import os
import re
from src.ingestion.pdf_extractor import extract_text_from_pdf
from src.ingestion.ocr_extractor import extract_text_from_image

SUPPORTED_IMAGES = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp'}
SUPPORTED_PDFS = {'.pdf'}

def detect_file_type(file_path: str) -> str:
    ext = os.path.splitext(file_path)[1].lower()
    if ext in SUPPORTED_PDFS:
        return 'pdf'
    elif ext in SUPPORTED_IMAGES:
        return 'image'
    else:
        raise ValueError(f"Unsupported file type: {ext}")

def clean_text(raw_text: str) -> str:
    text = re.sub(r' +', ' ', raw_text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'[^\x20-\x7E\n]', '', text)
    return text.strip()

def load_document(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    result = {
        'file_path': file_path,
        'file_type': None,
        'raw_text': '',
        'char_count': 0,
        'success': False
    }

    try:
        file_type = detect_file_type(file_path)
        result['file_type'] = file_type

        if file_type == 'pdf':
            raw_text = extract_text_from_pdf(file_path)
        else:
            raw_text = extract_text_from_image(file_path)

        cleaned = clean_text(raw_text)
        result['raw_text'] = cleaned
        result['char_count'] = len(cleaned)
        result['success'] = True
        print(f"[INFO] Extracted {len(cleaned)} characters")

    except Exception as e:
        print(f"[ERROR] {e}")
        result['error'] = str(e)

    return result