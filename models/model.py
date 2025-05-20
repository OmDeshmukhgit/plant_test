import torch
import torch.nn as nn
import torchvision.models as models

def get_model(num_classes):
    """
    Returns a ResNet18 model with the final layer adjusted for the given number of classes.
    Args:
        num_classes (int): Number of output classes
    Returns:
        torch.nn.Module: ResNet18 model
    """
    model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model

def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)