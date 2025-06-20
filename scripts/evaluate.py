import os
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from models.model import get_model
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuration
BATCH_SIZE = 32
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def evaluate_model(model, test_loader, device, class_names):
    model.eval()
    all_preds = []
    all_labels = []
    correct = 0
    total = 0
    running_loss = 0.0
    criterion = nn.CrossEntropyLoss()

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            running_loss += loss.item() * images.size(0)

            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    accuracy = correct / total
    average_loss = running_loss / total

    # Classification Report
    print("Classification Report:")
    print(classification_report(all_labels, all_preds, target_names=class_names))

    # Confusion Matrix
    cm = confusion_matrix(all_labels, all_preds)
    
    # Determine appropriate figure size based on number of classes
    num_classes = len(class_names)
    fig_width = max(12, num_classes * 0.8)  # Adjust width dynamically
    fig_height = max(10, num_classes * 0.7)  # Adjust height dynamically
    
    plt.figure(figsize=(fig_width, fig_height), dpi=300)  # Higher resolution
    
    # Create heatmap with improved readability
    sns.heatmap(cm, 
                annot=True,  # Show numbers
                fmt='d',     # Integer formatting
                cmap='YlGnBu',  # More color variation
                linewidths=0.5,  # Add grid lines
                cbar_kws={'label': 'Number of Samples'},
                square=True,  # Make cells square
                xticklabels=class_names, 
                yticklabels=class_names)
    
    plt.title('Confusion Matrix of Plant Leaf Disease Classification', fontsize=16, pad=20)
    plt.xlabel('Predicted Labels', fontsize=12, labelpad=10)
    plt.ylabel('True Labels', fontsize=12, labelpad=10)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45, ha='right', fontsize=8)
    plt.yticks(rotation=0, fontsize=8)
    
    plt.tight_layout()
    plt.savefig('ui/assets/confusion_matrix.png', bbox_inches='tight')
    plt.close()

    return average_loss, accuracy, all_preds, all_labels

if __name__ == "__main__":
    # Load the best model
    TEST_DATA_DIR = 'data/processed/Preprocessed Plant Diseases Dataset/valid'
    test_dataset = datasets.ImageFolder(TEST_DATA_DIR, transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ]))

    num_classes = len(test_dataset.classes)
    class_names = test_dataset.classes

    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

    best_model = get_model(num_classes).to(DEVICE)
    best_model.load_state_dict(torch.load('models/checkpoints/best_model.pth'))

    # Comprehensive Evaluation
    test_loss, test_accuracy, predictions, true_labels = evaluate_model(best_model, test_loader, DEVICE, class_names)

    print(f"\nTest Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")

    # Per-class accuracy analysis
    class_correct = [0] * num_classes
    class_total = [0] * num_classes

    for pred, true_label in zip(predictions, true_labels):
        class_correct[true_label] += int(pred == true_label)
        class_total[true_label] += 1

    print("\nPer-class Accuracy:")
    for i in range(num_classes):
        print(f"{class_names[i]}: {class_correct[i] / class_total[i] * 100:.2f}% ({class_correct[i]}/{class_total[i]})")