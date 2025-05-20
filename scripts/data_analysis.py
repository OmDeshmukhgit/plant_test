# Required imports
import os
import matplotlib.pyplot as plt


def count_images_per_class(folder_path):
    # Dictionary to store class-wise image counts
    class_counts = {}

    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return class_counts

    # Count images in each class directory
    for class_name in sorted(os.listdir(folder_path)):
        class_dir = os.path.join(folder_path, class_name)
        if not os.path.isdir(class_dir):
            continue
        image_files = os.listdir(class_dir)
        class_counts[class_name] = len(image_files)

    return class_counts


def plot_class_distribution(counts, title, filename):
    # Create bar plot of class distribution
    plt.figure(figsize=(14, 6))
    plt.bar(counts.keys(), counts.values())
    
    # Set plot labels and title
    plt.title(title)
    plt.xlabel('Class')
    plt.ylabel('Number of Images')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)
    plt.tight_layout()
    
    # Save and close the plot
    plt.savefig(filename)
    plt.close()


def main():
    # Set up data directories
    base_dir = 'data/raw'
    train_dir = os.path.join(base_dir, 'train')
    valid_dir = os.path.join(base_dir, 'valid')

    # Count images in training set
    print("Counting images per class in training set...")
    train_counts = count_images_per_class(train_dir)
    print("Counting images per class in validation set...")
    valid_counts = count_images_per_class(valid_dir)

    # Display training set statistics
    print("\nTrain class distribution:")
    for cls, count in train_counts.items():
        print(f"{cls}: {count}")
    print(f"Total training images: {sum(train_counts.values())}")

    # Display validation set statistics
    print("\nValidation class distribution:")
    for cls, count in valid_counts.items():
        print(f"{cls}: {count}")
    print(f"Total validation images: {sum(valid_counts.values())}")

    # Generate and save distribution plots
    plot_class_distribution(train_counts, 'Training Set Class Distribution', 'ui/assets/train_class_distribution.png')
    plot_class_distribution(valid_counts, 'Validation Set Class Distribution', 'ui/assets/valid_class_distribution.png')
    print("\nBar plots saved as 'ui/assets/train_class_distribution.png' and 'ui/assets/valid_class_distribution.png'.")

# Run main function if script is executed directly
if __name__ == "__main__":
    main()