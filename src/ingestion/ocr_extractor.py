import easyocr
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

_ocr_reader = None

def get_ocr_reader():
    global _ocr_reader
    if _ocr_reader is None:
        print("[INFO] Loading EasyOCR model...")
        _ocr_reader = easyocr.Reader(['en'], gpu=False)
    return _ocr_reader

def preprocess_image(image_path: str) -> np.ndarray:
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    if min(width, height) < 1000:
        scale = 1000 / min(width, height)
        img = img.resize((int(width * scale), int(height * scale)), Image.LANCZOS)
    img = ImageEnhance.Contrast(img).enhance(1.5)
    img = img.filter(ImageFilter.SHARPEN)
    return np.array(img)

def extract_text_from_image(image_path: str) -> str:
    reader = get_ocr_reader()
    print(f"[INFO] Processing image: {image_path}")
    img_array = preprocess_image(image_path)
    results = reader.readtext(img_array, detail=0, paragraph=True)
    return "\n".join(results)