import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from models.model import get_model
from tqdm import tqdm
import warnings
import time
import argparse

warnings.filterwarnings('ignore')

# Argument parser for batch size and num_workers
parser = argparse.ArgumentParser(description='Train plant disease model')
parser.add_argument('--batch-size', type=int, default=32, help='Batch size for training (default: 32)')
parser.add_argument('--num-workers', type=int, default=4, help='Number of DataLoader workers (default: 4)')
args = parser.parse_args()

# Config
DATA_DIR = 'data/processed'  # Updated to new preprocessed data
TRAIN_DIR = os.path.join(DATA_DIR, 'train')
VALID_DIR = os.path.join(DATA_DIR, 'valid')
BATCH_SIZE = args.batch_size
IMG_SIZE = 224  # Ensure this matches the preprocessing size
EPOCHS = 40  # Total epochs
START_EPOCH = 38  # Last completed epoch
LEARNING_RATE = 0.001
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
RESUME_CHECKPOINT = 'models/checkpoints/checkpoint_epoch_38.pth'  # Last checkpoint to resume from

if DEVICE.type != 'cuda':
    print("[WARNING] CUDA (GPU) not available. Training will be much slower on CPU.")
else:
    print("[INFO] Using GPU for training.")

# Data transforms
train_transforms = transforms.Compose([
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
valid_transforms = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])

# Datasets and loaders
train_dataset = datasets.ImageFolder(TRAIN_DIR, transform=train_transforms)
valid_dataset = datasets.ImageFolder(VALID_DIR, transform=valid_transforms)

use_cuda = torch.cuda.is_available()
pin_memory = True if use_cuda else False
num_workers = args.num_workers

train_loader = DataLoader(
    train_dataset, batch_size=BATCH_SIZE, shuffle=True,
    num_workers=num_workers, pin_memory=pin_memory, persistent_workers=True
)
valid_loader = DataLoader(
    valid_dataset, batch_size=BATCH_SIZE, shuffle=False,
    num_workers=num_workers, pin_memory=pin_memory, persistent_workers=True
)

def main():
    # Model
    num_classes = len(train_dataset.classes)
    model = get_model(num_classes).to(DEVICE)

    # Loss and optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    # Resume from checkpoint if exists
    if os.path.exists(RESUME_CHECKPOINT):
        print(f"Loading checkpoint {RESUME_CHECKPOINT}")
        checkpoint = torch.load(RESUME_CHECKPOINT)
        model.load_state_dict(checkpoint['model_state_dict'])
        optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
        best_acc = checkpoint['best_acc']
        start_epoch = checkpoint['epoch']
        print(f"Resuming training from epoch {start_epoch}")
    else:
        start_epoch = 0
        best_acc = 0.0

    print("Starting training...")

    if use_cuda:
        scaler = torch.cuda.amp.GradScaler()  # For mixed precision training
    else:
        scaler = None

    # Training loop
    for epoch in range(start_epoch, EPOCHS):
        epoch_start = time.time()
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        data_load_time = 0.0
        batch_start = time.time()
        train_bar = tqdm(train_loader, desc=f"Epoch {epoch+1}/{EPOCHS} [Train]", leave=False)
        for images, labels in train_bar:
            data_load_time += time.time() - batch_start
            images, labels = images.to(DEVICE, non_blocking=use_cuda), labels.to(DEVICE, non_blocking=use_cuda)
            optimizer.zero_grad()
            if use_cuda:
                with torch.cuda.amp.autocast():
                    outputs = model(images)
                    loss = criterion(outputs, labels)
            else:
                outputs = model(images)
                loss = criterion(outputs, labels)
            if scaler:
                scaler.scale(loss).backward()
                scaler.step(optimizer)
                scaler.update()
            else:
                loss.backward()
                optimizer.step()
            running_loss += loss.item() * images.size(0)
            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
            train_bar.set_postfix({
                'loss': running_loss / total if total > 0 else 0,
                'acc': correct / total if total > 0 else 0
            })
            batch_start = time.time()
        epoch_loss = running_loss / len(train_loader.dataset)
        epoch_acc = correct / len(train_loader.dataset)

        # Validation
        model.eval()
        val_correct = 0
        val_total = 0
        val_running_loss = 0.0
        val_bar = tqdm(valid_loader, desc=f"Epoch {epoch+1}/{EPOCHS} [Valid]", leave=False)
        with torch.no_grad():
            for images, labels in val_bar:
                images, labels = images.to(DEVICE, non_blocking=use_cuda), labels.to(DEVICE, non_blocking=use_cuda)
                if use_cuda:
                    with torch.cuda.amp.autocast():
                        outputs = model(images)
                        loss = criterion(outputs, labels)
                else:
                    outputs = model(images)
                    loss = criterion(outputs, labels)
                _, preds = torch.max(outputs, 1)
                val_correct += (preds == labels).sum().item()
                val_total += labels.size(0)
                val_running_loss += loss.item() * images.size(0)
        val_acc = val_correct / val_total
        val_loss = val_running_loss / val_total
        epoch_time = time.time() - epoch_start
        print(f"Epoch {epoch+1}/{EPOCHS} - Loss: {epoch_loss:.4f} - Acc: {epoch_acc:.4f} - Val Loss: {val_loss:.4f} - Val Acc: {val_acc:.4f}")
        print(f"Epoch {epoch+1} time: {epoch_time:.2f} seconds (Data loading: {data_load_time:.2f} seconds)")

        # Save best model
        if val_acc > best_acc:
            best_acc = val_acc
            torch.save(model.state_dict(), 'models/checkpoints/best_model.pth')
            print("Best model saved.")

        # Save checkpoint for this epoch
        checkpoint = {
            'epoch': epoch + 1,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'best_acc': best_acc
        }
        checkpoint_path = f'models/checkpoints/checkpoint_epoch_{epoch+1}.pth'
        torch.save(checkpoint, checkpoint_path)
        print(f"Checkpoint saved: {checkpoint_path}")

    print(f"Training complete. Best validation accuracy: {best_acc:.4f}")

if __name__ == "__main__":
    main() 