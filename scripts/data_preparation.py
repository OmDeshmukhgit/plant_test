# Required imports
import os
import argparse
from PIL import Image

def count_images_in_folder(folder_path, check_corrupt=False, sample_size=None):
    # Initialize counters
    class_counts = {}
    corrupt_images = []

    # Check if folder exists
    if not os.path.exists(folder_path):
        print(f"Folder not found: {folder_path}")
        return class_counts, corrupt_images

    # Process each class directory
    for class_name in sorted(os.listdir(folder_path)):
        class_dir = os.path.join(folder_path, class_name)
        if not os.path.isdir(class_dir):
            continue

        # Count images in class
        image_files = os.listdir(class_dir)
        class_counts[class_name] = len(image_files)

        # Check for corrupted images
        if check_corrupt:
            files_to_check = image_files if sample_size is None else image_files[:sample_size]
            for img_file in files_to_check:
                img_path = os.path.join(class_dir, img_file)
                try:
                    with Image.open(img_path) as img:
                        img.verify()
                except Exception:
                    corrupt_images.append(img_path)

    return class_counts, corrupt_images

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Dataset structure and summary script.")
    parser.add_argument('--check-corrupt', action='store_true', help='Check for corrupted images (slow)')
    parser.add_argument('--sample-size', type=int, default=None, help='Number of images to check per class for corruption (default: all)')
    args = parser.parse_args()

    # Set up data directories
    base_dir = os.path.join('data/raw', 'New Plant Diseases Dataset(Augmented)')
    train_dir = os.path.join(base_dir, 'train')
    valid_dir = os.path.join(base_dir, 'valid')

    # Process training set
    print("\n--- Training Set ---")
    train_counts, train_corrupt = count_images_in_folder(train_dir, check_corrupt=args.check_corrupt, sample_size=args.sample_size)
    for cls, count in train_counts.items():
        print(f"{cls}: {count} images")
    print(f"Total training classes: {len(train_counts)}")
    print(f"Total training images: {sum(train_counts.values())}")
    if args.check_corrupt:
        if train_corrupt:
            print(f"Corrupted training images: {len(train_corrupt)}")
            for img in train_corrupt:
                print(f"  Corrupt: {img}")
        else:
            print("No corrupted images found in training set.")

    # Process validation set
    print("\n--- Validation Set ---")
    valid_counts, valid_corrupt = count_images_in_folder(valid_dir, check_corrupt=args.check_corrupt, sample_size=args.sample_size)
    for cls, count in valid_counts.items():
        print(f"{cls}: {count} images")
    print(f"Total validation classes: {len(valid_counts)}")
    print(f"Total validation images: {sum(valid_counts.values())}")
    if args.check_corrupt:
        if valid_corrupt:
            print(f"Corrupted validation images: {len(valid_corrupt)}")
            for img in valid_corrupt:
                print(f"  Corrupt: {img}")
        else:
            print("No corrupted images found in validation set.")

# Run main function if script is executed directly
if __name__ == "__main__":
    main()
  