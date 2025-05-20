from graphviz import Digraph

# Create the diagram
diagram = Digraph('PlantLeafDiseaseDetection', comment='System Design', format='png')

# Global diagram attributes
diagram.attr(rankdir='TB', size='12,10', 
             fontname='Helvetica', 
             label='Plant Leaf Disease Detection System Design')
diagram.attr('node', shape='box', 
             style='filled', fillcolor='white', 
             fontname='Helvetica', fontsize='10', 
             color='black', penwidth='1.5')
diagram.attr('edge', color='black', penwidth='1.0')

# Data Acquisition and Preprocessing
with diagram.subgraph(name='cluster_0') as c0:
    c0.attr(label='Data Acquisition & Preprocessing', 
            style='filled', fillcolor='white', color='black')
    c0.node('dataset', 'Plant Image Dataset\n\nSource of raw plant leaf images\nMultiple plant types', 
            shape='cylinder')
    c0.node('preprocessing', 'Preprocessing\n\nImage Resizing & Normalization\n- Standardize dimensions\n- Normalize pixel values\n- Data augmentation')
    c0.node('segmentation', 'Segmentation (Optional)\n\nLeaf Isolation\n- Remove background\n- Focus on leaf area')
    c0.edge('dataset', 'preprocessing')
    c0.edge('preprocessing', 'segmentation')

# Feature Extraction and Model
with diagram.subgraph(name='cluster_1') as c1:
    c1.attr(label='Machine Learning Pipeline', 
            style='filled', fillcolor='white', color='black')
    c1.node('feature_extraction', 'Feature Extraction\n\nResNet18 Model\n- Extract features\n- Hierarchical representations')
    c1.node('classification', 'Classification\n\nDisease Prediction\n- Multi-class model\n- Confidence scores')
    c1.node('disease_mapping', 'Disease Information\n\nPrediction Details\n- Symptoms\n- Treatment recommendations')
    c1.edge('segmentation', 'feature_extraction')
    c1.edge('feature_extraction', 'classification')
    c1.edge('classification', 'disease_mapping')

# User Interface
diagram.node('ui', 'User Interface\n\nPyQt5 Desktop App\n- Image upload\n- Real-time detection\n- Detailed report', 
             shape='ellipse')

# Final Connections
diagram.edge('disease_mapping', 'ui')

# Render the diagram
diagram.render('system_design_diagram', view=False, cleanup=True)
print('Simple black and white system design diagram generated as system_design_diagram.png')