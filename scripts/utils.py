"""Utility functions for the Plant Leaf Disease Detection project."""

import os
import torch
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from torchvision import transforms

def load_image(image_path, transform=None):
    """Load and preprocess a single image.
    
    Args:
        image_path (str): Path to the image file
        transform (transforms.Compose, optional): Transformations to apply
        
    Returns:
        torch.Tensor: Preprocessed image tensor
    """
    image = Image.open(image_path).convert('RGB')
    if transform is None:
        transform = transforms.Compose([
            transforms.Resize(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    return transform(image).unsqueeze(0)

def predict_disease(model, image_tensor, class_names, device='cuda'):
    """Predict disease class for a given image tensor.
    
    Args:
        model (nn.Module): Trained PyTorch model
        image_tensor (torch.Tensor): Preprocessed image tensor
        class_names (list): List of class names
        device (str): Device to run inference on
        
    Returns:
        tuple: (predicted_class_name, confidence_score)
    """
    model.eval()
    with torch.no_grad():
        image_tensor = image_tensor.to(device)
        outputs = model(image_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)
        return class_names[predicted.item()], confidence.item()

def visualize_prediction(image_path, prediction, confidence, output_path=None):
    """Visualize the prediction results on the image.
    
    Args:
        image_path (str): Path to the original image
        prediction (str): Predicted class name
        confidence (float): Prediction confidence score
        output_path (str, optional): Path to save the visualization
    """
    image = Image.open(image_path).convert('RGB')
    plt.figure(figsize=(10, 6))
    plt.imshow(image)
    plt.title(f'Prediction: {prediction}\nConfidence: {confidence:.2%}')
    plt.axis('off')
    
    if output_path:
        plt.savefig(output_path, bbox_inches='tight', pad_inches=0)
        plt.close()
    else:
        plt.show()

def get_mean_std(dataloader):
    """Calculate mean and standard deviation of a dataset.
    
    Args:
        dataloader (DataLoader): PyTorch dataloader for the dataset
        
    Returns:
        tuple: (mean, std) for each channel
    """
    channels_sum = torch.zeros(3)
    channels_squared_sum = torch.zeros(3)
    num_batches = 0

    for data, _ in dataloader:
        channels_sum += torch.mean(data, dim=[0, 2, 3])
        channels_squared_sum += torch.mean(data ** 2, dim=[0, 2, 3])
        num_batches += 1
    
    mean = channels_sum / num_batches
    std = (channels_squared_sum / num_batches - mean ** 2) ** 0.5
    
    return mean, std

def create_directory(directory):
    """Create a directory if it doesn't exist.
    
    Args:
        directory (str): Path to the directory to create
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def example_helper():
    """Example helper function."""
    pass