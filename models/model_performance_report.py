import os
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from models.model import get_model
from sklearn.metrics import (
    precision_recall_fscore_support, 
    classification_report, 
    confusion_matrix
)

# Configuration
BATCH_SIZE = 32
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
OUTPUT_DIR = 'performance_reports'

def create_output_directory():
    """Create output directory if it doesn't exist."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_test_data():
    """Load test dataset."""
    test_transforms = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    
    TEST_DATA_DIR = 'data/processed/valid'
    test_dataset = datasets.ImageFolder(TEST_DATA_DIR, transform=test_transforms)
    test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
    
    return test_loader, test_dataset.classes

def evaluate_model(model, test_loader, device):
    """Comprehensive model evaluation."""
    model.eval()
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, preds = torch.max(outputs, 1)
            
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    return all_preds, all_labels

def generate_performance_metrics(true_labels, predictions, class_names):
    """Generate detailed performance metrics."""
    # Precision, Recall, F1-Score, Support
    precision, recall, f1, support = precision_recall_fscore_support(
        true_labels, predictions, labels=range(len(class_names)), average=None
    )
    
    # Create DataFrame
    metrics_df = pd.DataFrame({
        'Class': class_names,
        'Precision': precision,
        'Recall': recall,
        'F1-Score': f1,
        'Support': support
    })
    
    # Sort by F1-Score
    metrics_df = metrics_df.sort_values('F1-Score')
    
    return metrics_df

def plot_performance_metrics(metrics_df):
    """Create visualizations for performance metrics."""
    create_output_directory()
    
    # 1. Bar plot of F1-Scores
    plt.figure(figsize=(15, 8))
    plt.bar(metrics_df['Class'], metrics_df['F1-Score'])
    plt.title('F1-Score by Plant Disease Class')
    plt.xlabel('Plant Disease Classes')
    plt.ylabel('F1-Score')
    plt.xticks(rotation=90, fontsize=6)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'f1_scores.png'), dpi=300)
    plt.close()
    
    # 2. Heatmap of Precision, Recall, F1-Score
    plt.figure(figsize=(15, 10))
    metrics_pivot = metrics_df.melt(id_vars='Class', value_vars=['Precision', 'Recall', 'F1-Score'])
    metrics_pivot_df = metrics_pivot.pivot(index='Class', columns='variable', values='value')
    sns.heatmap(metrics_pivot_df, 
                annot=True, cmap='YlGnBu', fmt='.2f')
    plt.title('Performance Metrics Heatmap')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, 'performance_heatmap.png'), dpi=300)
    plt.close()
    
    # 3. Save metrics to CSV
    metrics_df.to_csv(os.path.join(OUTPUT_DIR, 'performance_metrics.csv'), index=False)

def main():
    # Load test data
    test_loader, class_names = load_test_data()
    
    # Load the best model
    num_classes = len(class_names)
    best_model = get_model(num_classes).to(DEVICE)
    best_model.load_state_dict(torch.load('models/checkpoints/best_model.pth'))
    
    # Evaluate model
    predictions, true_labels = evaluate_model(best_model, test_loader, DEVICE)
    
    # Generate performance metrics
    metrics_df = generate_performance_metrics(true_labels, predictions, class_names)
    
    # Print overall classification report
    print("Comprehensive Classification Report:")
    print(classification_report(true_labels, predictions, target_names=class_names))
    
    # Plot and save performance metrics
    plot_performance_metrics(metrics_df)
    
    print(f"\nPerformance reports saved in {OUTPUT_DIR}")
    print("Files generated:")
    print("1. f1_scores.png - Bar plot of F1-Scores")
    print("2. performance_heatmap.png - Performance Metrics Heatmap")
    print("3. performance_metrics.csv - Detailed Performance Metrics")

if __name__ == "__main__":
    main()
