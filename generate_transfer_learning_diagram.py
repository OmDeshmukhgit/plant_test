from graphviz import Digraph

# Create the diagram
diagram = Digraph('TransferLearning', comment='Transfer Learning Diagram', format='png')

# Global diagram attributes
diagram.attr(rankdir='TB', size='10,8', 
             fontname='Helvetica', 
             label='Transfer Learning for Plant Leaf Disease Detection')
diagram.attr('node', shape='box', 
             style='filled', fillcolor='lightblue', 
             fontname='Helvetica', fontsize='10', 
             color='black', penwidth='1.5')
diagram.attr('edge', color='black', penwidth='1.0')

# Pretrained Model
diagram.node('pretrained', 'Pretrained Model\n\nResNet18\n- Trained on ImageNet\n- Extracts features from images')

# Fine-tuning Process
diagram.node('fine_tuning', 'Fine-tuning\n\n- Replace final layer\n- Train on plant disease dataset\n- Adjust weights')

# New Model
diagram.node('new_model', 'New Model\n\nCustomized for Plant Leaf Disease\n- Outputs disease classes\n- Confidence scores')

# Connections
diagram.edge('pretrained', 'fine_tuning')
diagram.edge('fine_tuning', 'new_model')

# Render the diagram
diagram.render('transfer_learning_diagram', view=False, cleanup=True)
print('Transfer learning diagram generated as transfer_learning_diagram.png')
