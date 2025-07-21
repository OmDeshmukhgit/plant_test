import streamlit as st
import torch
from PIL import Image
import torch.nn.functional as F
from models.model import get_model
from disease_info.disease_info_com import DISEASE_INFO
import os
import urllib.request
from urllib.parse import parse_qs

# --- Accessible, high-contrast CSS for result and info boxes and horizontal scroll gallery ---
st.markdown(
    """
    <style>
    body, .stApp { background: linear-gradient(135deg, #f4f7fa 0%, #e3e9ee 100%) !important; font-family: 'Segoe UI', 'Arial', sans-serif; }
    .result-card {
        background: #fff;
        border-radius: 16px;
        box-shadow: 0 2px 16px rgba(76,175,80,0.10);
        padding: 2em 1.5em;
        margin: 1.5em 0 1em 0;
        border-left: 8px solid #388e3c;
        color: #222;
    }
    .result-card h2 {
        color: #2e7d32 !important;
        font-weight: 700;
    }
    .disease-info-box {
        background: #e6f4ea;
        border-radius: 10px;
        padding: 1em;
        margin-bottom: 1em;
        border-left: 5px solid #388e3c;
        font-size: 1.1em;
        color: #222;
    }
    .disease-info-box b {
        color: #2e7d32;
    }
    .section-label {
        color: #388e3c;
        font-weight: 600;
        margin-top: 2em;
        margin-bottom: 0.5em;
        font-size: 1.2em;
    }
    .advanced-details {
        background: #f7fafc;
        border-radius: 10px;
        padding: 1em 1em 0.5em 1em;
        margin-top: 2em;
        border: 1px solid #cfd8dc;
    }
    .sample-thumb-img {
        width: 90px;
        height: 90px;
        object-fit: cover;
        border-radius: 8px;
        border: 2px solid #cfd8dc;
        margin-bottom: 0.3em;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    .sample-thumb-img.selected {
        border: 2px solid #388e3c;
        box-shadow: 0 2px 8px rgba(56,142,60,0.12);
    }
    .sample-btn {
        margin-bottom: 0.2em;
    }
    .sample-gallery {
        display: flex;
        overflow-x: auto;
        padding-bottom: 0.5em;
        margin-bottom: 1em;
    }
    .sample-item {
        flex: 0 0 auto;
        margin-right: 1em;
        text-align: center;
    }
    .stExpander, .stExpanderHeader {
        background: #f5f5f5 !important;
        color: #222 !important;
        border-radius: 8px !important;
        border: 1px solid #cfd8dc !important;
    }
    .stExpander[aria-expanded="true"] > div > div {
        background: #f7fafc !important;
    }
    @media (max-width: 600px) {
        .result-card { padding: 1em 0.5em; font-size: 1em; }
        .disease-info-box { font-size: 1em; }
        .section-label { font-size: 1em; }
        .sample-thumb-img { width: 60px; height: 60px; }
    }
    .stImage>img { max-width: 100% !important; height: auto !important; }
    .sample-use-btn button {
        background-color: #43a047 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 1em !important;
        margin-bottom: 0.2em;
        padding: 0.5em 1.2em !important;
        box-shadow: 0 1px 4px rgba(67,160,71,0.08);
        transition: background 0.2s;
    }
    .sample-gallery > div button {
        background-color: #43a047 !important;
        color: #fff !important;
        border: none !important;
        border-radius: 6px !important;
        font-weight: 600 !important;
        font-size: 1em !important;
        margin-bottom: 0.2em;
        padding: 0.5em 1.2em !important;
        box-shadow: 0 1px 4px rgba(67,160,71,0.08);
        transition: background 0.2s;
    }
    .sample-gallery > div button:hover {
        background-color: #388e3c !important;
        color: #fff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Helper Functions ---
@st.cache_resource
def load_model():
    num_classes = len(DISEASE_INFO)
    model = get_model(num_classes)
    model.load_state_dict(torch.load('models/checkpoints/best_model.pth', map_location='cpu'))
    model.eval()
    return model

def transform_image(image):
    from torchvision import transforms
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    return transform(image).unsqueeze(0)

# --- Streamlit UI ---
st.set_page_config(page_title="Plantest", layout="wide")
st.markdown("<h1 style='text-align:center; color:#388e3c; margin-bottom:0.2em;'>🌱 Plantest</h1>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:#666; font-size:1.1em;'>Upload a plant leaf image and instantly get a disease diagnosis!</div>", unsafe_allow_html=True)

# Language selection
def get_language_code(lang):
    if lang == "English": return "en"
    if lang == "Hindi": return "hi"
    if lang == "Marathi": return "mr"
    return "en"

lang = st.selectbox("Select Language / भाषा निवडा", ["English", "Hindi", "Marathi"])
language_code = get_language_code(lang)

# Download model from Google Drive if not present
model_path = 'models/checkpoints/best_model.pth'
gdrive_file_id = '1AK7QJkTl0i4HqpaKBNoL1FHDj1cICnng'

if not os.path.exists(model_path):
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    st.info('Downloading model file from Google Drive. This may take a while...')
    import gdown
    url = f'https://drive.google.com/uc?id={gdrive_file_id}'
    gdown.download(url, model_path, quiet=False)
    st.success('Model download complete!')

model = load_model()
class_names = [DISEASE_INFO[i][language_code]['name'] if isinstance(DISEASE_INFO[i], dict) and language_code in DISEASE_INFO[i] and 'name' in DISEASE_INFO[i][language_code] else DISEASE_INFO[i].get('name', f'Class {i}') for i in range(len(DISEASE_INFO))]

# --- Sample Images Section (Gallery Only, No Dropdown, No Filenames) ---
sample_dir = "samples"
sample_images = []
if os.path.exists(sample_dir):
    for fname in sorted(os.listdir(sample_dir)):
        if fname.lower().endswith((".jpg", ".jpeg", ".png")):
            sample_images.append(os.path.join(sample_dir, fname))

selected_sample = st.session_state.get('selected_sample', None)

if sample_images:
    with st.expander("🌿 Try with Sample Image", expanded=False):
        display_images = sample_images[:2]  # Only the first two images
        cols = st.columns(2)
        for i, img_path in enumerate(display_images):
            with cols[i]:
                st.image(img_path, width=90)
                st.markdown('<div class="sample-use-btn">', unsafe_allow_html=True)
                if st.button("Use", key=f"sample_btn_{img_path}"):
                    st.session_state['selected_sample'] = img_path
                st.markdown('</div>', unsafe_allow_html=True)

# --- Image Upload and Prediction ---
st.markdown("<div class='section-label'>1️⃣ Upload a leaf image for disease prediction</div>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# --- Determine which image to use for prediction ---
image_to_predict = None
if st.session_state.get('selected_sample'):
    image_to_predict = st.session_state['selected_sample']
elif uploaded_file is not None:
    image_to_predict = uploaded_file

if image_to_predict is not None:
    if isinstance(image_to_predict, str):
        image = Image.open(image_to_predict).convert("RGB")
    else:
        image = Image.open(image_to_predict).convert("RGB")
    st.image(image, caption="Selected Image", use_container_width=True)
    input_tensor = transform_image(image)
    with torch.no_grad():
        outputs = model(input_tensor)
        probabilities = F.softmax(outputs, dim=1)
        top_prob, top_class = torch.topk(probabilities, 1)
        class_idx = top_class[0][0].item()
        prob = top_prob[0][0].item() * 100
        disease_info = DISEASE_INFO[class_idx]
        # --- Get language-specific info ---
        lang_info = disease_info.get(language_code, {}) if isinstance(disease_info, dict) else {}
        disease_name = lang_info.get('name', class_names[class_idx])
        st.markdown(f"""
        <div class='result-card'>
            <h2>🌟 Prediction Result</h2>
            <div style='font-size:1.3em;'><b>{disease_name}</b> <span style='color:#444;'>(Confidence: {prob:.2f}%)</span></div>
        </div>
        """, unsafe_allow_html=True)
        # --- Disease info box ---
        description = lang_info.get('description', '-')
        symptoms = ', '.join(lang_info.get('symptoms', [])) if isinstance(lang_info.get('symptoms', []), list) else lang_info.get('symptoms', '-')
        causes = ', '.join(lang_info.get('causes', [])) if isinstance(lang_info.get('causes', []), list) else lang_info.get('causes', '-')
        treatments = ', '.join(lang_info.get('treatments', [])) if isinstance(lang_info.get('treatments', []), list) else lang_info.get('treatments', '-')
        st.markdown(f"""
        <div class='disease-info-box'>
            <b>Description:</b> {description}<br>
            <b>Symptoms:</b> {symptoms}<br>
            <b>Causes:</b> {causes}<br>
            <b>Treatments:</b> {treatments}
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("Please upload a clear image of a plant leaf or select a sample image to get started.")

# --- Advanced Details Section ---
st.markdown("<div class='section-label'>🔬 Advanced Details (for technical viewers)</div>", unsafe_allow_html=True)
st.markdown("<div style='color:#888; font-size:0.98em; margin-bottom:0.5em;'>Expand the sections below to see model performance, class distribution, and system diagrams.</div>", unsafe_allow_html=True)
st.markdown("<div class='advanced-details'>", unsafe_allow_html=True)

with st.expander("Confusion Matrix", expanded=False):
    if os.path.exists("ui/assets/confusion_matrix.png"):
        st.image("ui/assets/confusion_matrix.png", caption="Confusion Matrix", use_container_width=True)
    else:
        st.info("Confusion matrix image not found.")
with st.expander("F1 Scores & Heatmap", expanded=False):
    if os.path.exists("performance_reports/f1_scores.png"):
        st.image("performance_reports/f1_scores.png", caption="F1 Scores", use_container_width=True)
    if os.path.exists("performance_reports/performance_heatmap.png"):
        st.image("performance_reports/performance_heatmap.png", caption="Performance Heatmap", use_container_width=True)
with st.expander("Train Class Distribution", expanded=False):
    if os.path.exists("ui/assets/train_class_distribution.png"):
        st.image("ui/assets/train_class_distribution.png", caption="Train Class Distribution", use_container_width=True)
with st.expander("Validation Class Distribution", expanded=False):
    if os.path.exists("ui/assets/valid_class_distribution.png"):
        st.image("ui/assets/valid_class_distribution.png", caption="Validation Class Distribution", use_container_width=True)
with st.expander("System Design Diagram", expanded=False):
    if os.path.exists("ui/assets/system_design_diagram.png"):
        st.image("ui/assets/system_design_diagram.png", caption="System Design Diagram", use_container_width=True)
with st.expander("Transfer Learning Diagram", expanded=False):
    if os.path.exists("ui/assets/transfer_learning_diagram.png"):
        st.image("ui/assets/transfer_learning_diagram.png", caption="Transfer Learning Diagram", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; color:#388e3c; margin-top:2em;'>Made with OmDev.</div>", unsafe_allow_html=True) 