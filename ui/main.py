import os
import sys
import warnings

# Suppress specific font warnings
warnings.filterwarnings('ignore', category=UserWarning, module='PyQt5')
import torch
import numpy as np
from PIL import Image
import torch.nn.functional as F
from disease_info.disease_info_com import DISEASE_INFO
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, QTextEdit, QProgressBar, QTabWidget, QGroupBox, QFrame, QComboBox
)
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt
from models.model import get_model

class PlantDiseaseDetectorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Plant Disease Detection')
        self.setMinimumSize(1200, 900)
        
        # Use a system-compatible font
        app_font = QFont('Segoe UI', 10)
        QApplication.setFont(app_font)
        
        self.setStyleSheet("QMainWindow { background-color: #fff; }")
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = self._load_model()
        self.class_names = self._load_class_names()
        self.image_path = None
        self._init_ui()

    def _init_ui(self):
        # Tabs
        tabs = QTabWidget()
        tabs.setStyleSheet("QTabBar::tab { min-width: 120px; min-height: 28px; font-size: 13px; padding: 4px 16px; } QTabBar::tab:selected { background: #e8f5e9; border: 1px solid #4CAF50; border-bottom: none; } QTabBar::tab:!selected { background: #f5f5f5; border: 1px solid #bdbdbd; border-bottom: none; }")
        prediction_tab = QWidget()
        tabs.addTab(prediction_tab, "Prediction")
        self.setCentralWidget(tabs)

        # Main layout for Prediction tab
        main_layout = QVBoxLayout()
        prediction_tab.setLayout(main_layout)

        # Header
        header = QLabel("Plant Disease Detection System")
        header.setAlignment(Qt.AlignCenter)
        header.setFont(QFont("Arial", 18, QFont.Bold))
        header_frame = QFrame()
        header_frame.setFrameShape(QFrame.Box)
        header_frame.setLineWidth(2)
        header_frame.setStyleSheet("QFrame { border: 2px solid #4CAF50; border-radius: 4px; background: #fff; }")
        header_layout = QVBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.addWidget(header)
        header_frame.setLayout(header_layout)
        main_layout.addWidget(header_frame)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Main content area (left and right)
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout, 1)

        # Left panel (Image upload)
        left_panel = QVBoxLayout()
        content_layout.addLayout(left_panel, 2)

        # Image drop/upload area
        image_group = QGroupBox()
        image_group.setStyleSheet("QGroupBox { border: 2px dashed #43a047; border-radius: 12px; margin-top: 8px; background: #fff; min-height: 600px; } ")
        image_group.setTitle("")
        image_group_layout = QVBoxLayout()
        image_group_layout.setContentsMargins(20, 20, 20, 20)
        self.image_display = QLabel("Drag and drop an image here\n or click to select", self)
        self.image_display.setAlignment(Qt.AlignCenter)
        self.image_display.setAcceptDrops(True)
        self.image_display.setStyleSheet("QLabel { color: #444; font-size: 18px; font-weight: bold; padding: 20px; border: none; min-width: 400px; min-height: 320px; }")        
        image_group_layout.addWidget(self.image_display)
        image_group.setLayout(image_group_layout)
        left_panel.addWidget(image_group)

        # Buttons
        button_layout = QHBoxLayout()
        self.upload_btn = QPushButton(" Upload Image")
        self.upload_btn.setIcon(QIcon.fromTheme("folder"))
        self.upload_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-size: 15px; min-width: 180px; } QPushButton:hover { background-color: #388e3c; }")
        self.upload_btn.clicked.connect(self.upload_image)
        button_layout.addWidget(self.upload_btn)
        self.detect_btn = QPushButton("Detect Disease")
        self.detect_btn.setEnabled(False)
        self.detect_btn.setStyleSheet("QPushButton { background-color: #f5f5f5; color: #bdbdbd; border: 1px solid #ccc; padding: 10px 20px; border-radius: 5px; font-size: 15px; min-width: 180px; }")       
        self.detect_btn.clicked.connect(self.detect_disease)
        button_layout.addWidget(self.detect_btn)
        left_panel.addLayout(button_layout)
        
        # Language Selection
        language_layout = QHBoxLayout()
        language_label = QLabel("Language ( भाषा निवडा ) :")
        language_label.setStyleSheet("color:rgb(0, 0, 0); font-weight: 600; font-size: 24px; margin-left: 0px;")
        self.language_dropdown = QComboBox()
        self.language_dropdown.addItems(["English", "Hindi", "Marathi"])
        self.language_dropdown.setStyleSheet("""
            QComboBox {
                background-color: #f5f5f5;
                color: #333;
                border: 1px solid #4CAF50;
                border-radius: 5px;
                padding: 5px;
                min-width: 150px;
                font-size: 14px;
                font-weight: bold;
                padding-right: 30px;  /* Make room for the arrow */
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left: 1px solid #4CAF50;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
            }
            QComboBox::down-arrow {
                image: url(ui/arrow_icon.png);
                width: 16px;
                height: 16px;
            }
        """)
        language_layout.addWidget(language_label)
        language_layout.addWidget(self.language_dropdown)
        left_panel.addLayout(language_layout)
        
        left_panel.addStretch(1)

        # Right panel (Detection Results)
        right_panel = QVBoxLayout()
        content_layout.addLayout(right_panel, 3)
        # Detection Results header
        results_header = QLabel("Detection Results")
        results_header.setFont(QFont("Arial", 13, QFont.Bold))
        results_header.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        results_header_frame = QFrame()
        results_header_frame.setFrameShape(QFrame.Box)
        results_header_frame.setLineWidth(2)
        results_header_frame.setStyleSheet("QFrame { background: #f0f0f0; padding: 10px; border-radius: 0px; }")
        results_header_layout = QVBoxLayout()
        results_header_layout.setContentsMargins(12, 2, 12, 2)
        results_header_layout.addWidget(results_header)
        results_header_frame.setLayout(results_header_layout)
        right_panel.addWidget(results_header_frame)
        # Results display area
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("QTextEdit { border: 1px solid #bdbdbd; border-radius: 8px; background: #fff; font-size: 15px; font-weight: bold; min-height: 620px; margin-top: 8px; }")
        right_panel.addWidget(self.result_text)
        right_panel.addStretch(1)

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if file_name:
            self.image_path = file_name
            self.display_image(file_name)
            self.detect_btn.setEnabled(True)
            self.detect_btn.setStyleSheet("QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px 20px; border-radius: 5px; font-size: 15px; min-width: 180px; } QPushButton:hover { background-color: #388e3c; }")

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(400, 320, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_display.setPixmap(scaled_pixmap)
        self.image_display.setStyleSheet("QLabel { border: none; min-width: 400px; min-height: 320px; }")

    def detect_disease(self):
        if not self.image_path:
            self.result_text.setText("❌ Please upload an image first.")
            return
        try:
            image = Image.open(self.image_path).convert("RGB")
            transform = self._get_transform()
            input_tensor = transform(image).unsqueeze(0).to(self.device)
            with torch.no_grad():
                outputs = self.model(input_tensor)
                probabilities = F.softmax(outputs, dim=1)
                top_prob, top_class = torch.topk(probabilities, 1)
            result = "\U0001F4CA Detailed Disease Analysis\n\n"
            class_idx = top_class[0][0].item()
            class_name = self.class_names[class_idx]
            prob = top_prob[0][0].item() * 100
            # Translate disease name based on selected language
            selected_language = 'en' if self.language_dropdown.currentText() == 'English' else 'hi' if self.language_dropdown.currentText() == 'Hindi' else 'mr'
            
            # Get the disease translation directly using the class index
            disease_info = DISEASE_INFO.get(class_idx, {})
            
            # Select the appropriate translation based on language
            if selected_language == 'en':
                translated_class_name = disease_info.get('en', {}).get('name', class_name)
            elif selected_language == 'hi':
                translated_class_name = disease_info.get('hi', {}).get('name', class_name)
            else:  # Marathi
                translated_class_name = disease_info.get('mr', {}).get('name', class_name)
            
            # Clean up the translated name
            translated_class_name = translated_class_name.replace('___', ' ').replace('_', ' ')
            
            result += f"1. {translated_class_name}: {prob:.2f}%\n"
            
            # Get disease details in the selected language
            disease_details = DISEASE_INFO.get(class_idx, {}).get(selected_language, DISEASE_INFO.get(class_idx, {}).get('en', {}))
            if disease_details:
                description = disease_details.get('description', '-')
                symptoms = '\n         - '.join(disease_details.get('symptoms', []))
                causes = '\n         - '.join(disease_details.get('causes', []))
                treatments = '\n         - '.join(disease_details.get('treatments', []))
                result += f"   Description: {description}\n"
                result += f"   Symptoms:\n      - {symptoms}\n"
                result += f"   Causes:\n      - {causes}\n"
                result += f"   Treatments:\n      - {treatments}\n\n"
            else:
                result += f"   [No detailed info available]\n\n"
            self.result_text.setText(result)
        except Exception as e:
            self.result_text.setText(f"❌ Error in prediction: {str(e)}")

    def _load_model(self):
        model = get_model(len(self._load_class_names())).to(self.device)
        model.load_state_dict(torch.load('models/checkpoints/best_model.pth', map_location=self.device))
        model.eval()
        return model

    def _load_class_names(self):
        return sorted(os.listdir('data/processed/Preprocessed Plant Diseases Dataset/valid'))

    def _get_transform(self):
        from torchvision import transforms
        return transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

def main():
    app = QApplication(sys.argv)
    main_window = PlantDiseaseDetectorApp()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()