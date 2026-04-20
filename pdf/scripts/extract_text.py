import sys
from pypdf import PdfReader

reader = PdfReader(sys.argv[1])
text = ""

for page in reader.pages:
    text += page.extract_text() or ""

print(text)