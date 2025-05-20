
# Plant Leaf Disease Detection

This project uses deep learning to detect diseases in plant leaves from images. The dataset is organized into training and validation folders, each containing subfolders for each disease or healthy class.

## Project Structure

- `data_preparation.py`: Prepare and preprocess the dataset
- `data_analysis.py`: Analyze and visualize the dataset
- `model.py`: Define the deep learning model
- `train.py`: Train the model
- `evaluate.py`: Evaluate the trained model
- `requirements.txt`: Project dependencies

## Setup Instructions

1. (Optional) Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Prepare the data:
   ```bash
   python data_preparation.py
   ```
4. Analyze the data:
   ```bash
   python data_analysis.py
   ```
5. Train the model:
   ```bash
   python train.py
   ```
6. Evaluate the model:
   ```bash
   python evaluate.py
   ```

## Dataset

- Place your dataset in the `New Plant Diseases Dataset(Augmented)` folder, with `train` and `valid` subfolders.

## Goals

- Achieve high accuracy in classifying plant leaf diseases
- Provide clear visualizations and reports
- Build a robust, extensible codebase
>>>>>>> a3b68a8 (Initial commit)
