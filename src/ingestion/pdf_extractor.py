import pdfplumber
import fitz
import easyocr
import numpy as np
import os

_ocr_reader = None

def get_ocr_reader():
    global _ocr_reader
    if _ocr_reader is None:
        print("[INFO] Loading EasyOCR model...")
        _ocr_reader = easyocr.Reader(['en'], gpu=False)
    return _ocr_reader

def is_scanned_pdf(file_path: str, threshold: int = 10) -> bool:
    with pdfplumber.open(file_path) as pdf:
        pages_to_check = min(3, len(pdf.pages))
        total_text = ""
        for i in range(pages_to_check):
            text = pdf.pages[i].extract_text()
            if text:
                total_text += text
        avg_chars = len(total_text) / pages_to_check
        print(f"[INFO] Avg chars/page: {avg_chars:.1f}")
        return avg_chars < threshold

def extract_text_from_digital_pdf(file_path: str) -> str:
    text_pages = []
    with pdfplumber.open(file_path) as pdf:
        print(f"[INFO] Total pages: {len(pdf.pages)}")
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                text_pages.append(f"\n--- Page {i+1} ---\n{page_text}")
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    rows = []
                    for row in table:
                        cleaned = [str(cell).strip() if cell else "" for cell in row]
                        rows.append(" | ".join(cleaned))
                    text_pages.append("\n".join(rows))
    return "\n\n".join(text_pages).strip()

def extract_text_from_scanned_pdf(file_path: str) -> str:
    reader = get_ocr_reader()
    text_pages = []
    pdf_document = fitz.open(file_path)
    for page_num in range(len(pdf_document)):
        print(f"[INFO] OCR page {page_num+1}...")
        page = pdf_document[page_num]
        mat = fitz.Matrix(2, 2)
        pix = page.get_pixmap(matrix=mat)
        img_array = np.frombuffer(pix.samples, dtype=np.uint8)
        img_array = img_array.reshape(pix.height, pix.width, pix.n)
        results = reader.readtext(img_array, detail=0)
        text_pages.append(f"\n--- Page {page_num+1} ---\n{' '.join(results)}")
    pdf_document.close()
    return "\n\n".join(text_pages).strip()

def extract_text_from_pdf(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"PDF not found: {file_path}")
    print(f"[INFO] Processing: {file_path}")
    if is_scanned_pdf(file_path):
        print("[INFO] → Scanned PDF. Using OCR.")
        return extract_text_from_scanned_pdf(file_path)
    else:
        print("[INFO] → Digital PDF. Extracting text.")
        return extract_text_from_digital_pdf(file_path)