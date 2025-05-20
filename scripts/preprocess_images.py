# Required imports
import os
from PIL import Image
from tqdm import tqdm

# Define constants for image processing
SRC_BASE_DIR = 'data/raw'
DST_BASE_DIR = 'data/processed'
IMG_SIZE = 224  # Target size for all images

# Process both training and validation sets
splits = ['train', 'valid']

# Process each split (train/valid)
for split in splits:
    # Set up source and destination directories
    src_dir = os.path.join(SRC_BASE_DIR, split)
    dst_dir = os.path.join(DST_BASE_DIR, split)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Process each class directory
    for class_name in sorted(os.listdir(src_dir)):
        # Set up class-specific directories
        src_class_dir = os.path.join(src_dir, class_name)
        dst_class_dir = os.path.join(dst_dir, class_name)
        if not os.path.exists(dst_class_dir):
            os.makedirs(dst_class_dir)

        # Get list of images to process
        image_files = os.listdir(src_class_dir)

        # Process each image with progress bar
        for img_file in tqdm(image_files, desc=f"{split}/{class_name}"):
            src_img_path = os.path.join(src_class_dir, img_file)
            dst_img_path = os.path.join(dst_class_dir, img_file)

            # Skip if image already processed
            if os.path.exists(dst_img_path):
                continue

            try:
                # Load, convert to RGB, resize, and save image
                with Image.open(src_img_path) as img:
                    img = img.convert('RGB')  # Ensure consistent color format
                    img = img.resize((IMG_SIZE, IMG_SIZE), Image.BILINEAR)
                    img.save(dst_img_path)
            except Exception as e:
                print(f"Failed to process {src_img_path}: {e}")

print("Preprocessing complete! All images resized and saved to:", DST_BASE_DIR)