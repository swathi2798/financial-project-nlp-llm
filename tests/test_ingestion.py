import sys
import os

# This tells Python where to find the src folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ingestion.document_loader import load_document

print("=" * 50)
print("TESTING DOCUMENT LOADER")
print("=" * 50)

test_pdf = os.path.join(os.path.dirname(__file__), '..', 'data', 'sample_statements', 'test.pdf')
test_pdf = os.path.abspath(test_pdf)

if os.path.exists(test_pdf):
    result = load_document(test_pdf)
    print(f"Success:    {result['success']}")
    print(f"File type:  {result['file_type']}")
    print(f"Characters: {result['char_count']}")
    print(f"\nPreview:\n{result['raw_text'][:300]}")
else:
    print(f"[ERROR] No PDF found at {test_pdf}")