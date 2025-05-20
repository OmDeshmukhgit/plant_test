import re
import json
from googletrans import Translator

# Path to your disease_info_com.py
DISEASE_INFO_PATH = 'disease_info/disease_info_com.py'

def extract_english_entries():
    """Extract English disease entries more robustly by parsing line by line"""
    with open(DISEASE_INFO_PATH, 'r', encoding='utf-8') as f:
        content = f.readlines()
    
    # Manual parsing approach
    disease_info = {}
    current_id = None
    current_field = None
    current_data = {}
    in_list = False
    list_data = []
    
    for line in content:
        line = line.strip()
        
        # Start of a new disease entry
        if re.match(r'^\s*\d+\s*:\s*{', line):
            if current_id is not None:
                disease_info[current_id] = current_data
            current_id = int(re.match(r'^\s*(\d+)\s*:', line).group(1))
            current_data = {}
            
        # Language entry (skip non-English)
        elif re.match(r'^\s*"(en|hi|mr)"\s*:\s*{', line):
            lang = re.match(r'^\s*"(en|hi|mr)"\s*:', line).group(1)
            if lang == "en":
                current_data = {}  # Reset for English data
            else:
                continue  # Skip non-English
                
        # Non-language entry (for older format)
        elif re.match(r'^\s*"name"\s*:', line) and not current_data:
            # This is the old format without language keys
            current_data = {}
            
        # Field start
        elif re.match(r'^\s*"([^"]+)"\s*:\s*"([^"]+)"', line):
            match = re.match(r'^\s*"([^"]+)"\s*:\s*"([^"]+)"', line)
            field, value = match.groups()
            current_data[field] = value.rstrip(',')
            
        elif re.match(r'^\s*"([^"]+)"\s*:\s*"', line):
            match = re.match(r'^\s*"([^"]+)"\s*:\s*"', line)
            field = match.group(1)
            value = line.split(':', 1)[1].strip().strip('"').rstrip('",')
            current_data[field] = value
            
        # List start
        elif re.match(r'^\s*"([^"]+)"\s*:\s*\[', line):
            current_field = re.match(r'^\s*"([^"]+)"\s*:', line).group(1)
            in_list = True
            list_data = []
            
        # List item
        elif in_list and re.match(r'^\s*"[^"]+"', line):
            item = line.strip().strip('"').rstrip('",')
            list_data.append(item)
            
        # List end
        elif in_list and "]" in line:
            current_data[current_field] = list_data
            in_list = False
            current_field = None
            
        # End of an entry
        elif line.startswith('},') or line.startswith('}'):
            if current_id is not None and current_data:
                disease_info[current_id] = current_data.copy()
    
    # Add the last entry if there is one
    if current_id is not None and current_id not in disease_info:
        disease_info[current_id] = current_data
        
    return disease_info

def translate_text(text, dest, translator):
    if not text:
        return text
    if isinstance(text, list):
        return [translate_text(t, dest, translator) for t in text]
    try:
        return translator.translate(text, dest=dest).text
    except Exception as e:
        print(f"Translation error: {e} for text: {text}")
        return text

def main():
    disease_info = extract_english_entries()
    translator = Translator()
    translations = {}

    for idx, entry in disease_info.items():
        # Skip entries with no name
        if 'name' not in entry:
            continue
            
        disease_key = entry['name']
        translations[disease_key] = {}
        # English
        translations[disease_key]['english'] = {
            'name': entry.get('name', ''),
            'description': entry.get('description', ''),
            'symptoms': entry.get('symptoms', []),
            'causes': entry.get('causes', []),
            'treatments': entry.get('treatments', []),
        }
        
        print(f"Processing: {disease_key}")
        
        # Hindi
        translations[disease_key]['hindi'] = {
            'name': translate_text(entry.get('name', ''), 'hi', translator),
            'description': translate_text(entry.get('description', ''), 'hi', translator),
            'symptoms': translate_text(entry.get('symptoms', []), 'hi', translator),
            'causes': translate_text(entry.get('causes', []), 'hi', translator),
            'treatments': translate_text(entry.get('treatments', []), 'hi', translator),
        }
        
        # Marathi
        translations[disease_key]['marathi'] = {
            'name': translate_text(entry.get('name', ''), 'mr', translator),
            'description': translate_text(entry.get('description', ''), 'mr', translator),
            'symptoms': translate_text(entry.get('symptoms', []), 'mr', translator),
            'causes': translate_text(entry.get('causes', []), 'mr', translator),
            'treatments': translate_text(entry.get('treatments', []), 'mr', translator),
        }
        
        print(f"Translated: {disease_key}")

    # Output as Python code
    with open('disease_info/translated_output.py', 'w', encoding='utf-8') as f:
        f.write('TRANSLATIONS = ')
        f.write(json.dumps(translations, indent=4, ensure_ascii=False))
    
    print('Translation complete! Output written to disease_info/translated_output.py')
    print(f'Processed {len(translations)} diseases')

if __name__ == '__main__':
    main()