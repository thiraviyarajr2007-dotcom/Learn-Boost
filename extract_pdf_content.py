# /// script
# requires-python = ">=3.8"
# dependencies = ["PyPDF2"]
# ///

import PyPDF2
import json
import re

def extract_pdf_text(pdf_path):
    """Extract text from PDF file"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

# Path to the PDF files
pdf_paths = [
    r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\Learning edu\Tn sylubus\Class_2_Mathematics_English_Medium-Term_1-2024_Edition-www.tntextbooks.in.pdf",
    r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\Learning edu\Tn sylubus\Class_2_Mathematics_English_Medium-Term_2-2024_Edition-www.tntextbooks.in.pdf",
    r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\Learning edu\Tn sylubus\Class_2_Mathematics_English_Medium-Term_3-2024_Edition-www.tntextbooks.in.pdf"
]

# Extract content from all PDFs
all_content = {}
for i, pdf_path in enumerate(pdf_paths, 1):
    print(f"Extracting content from Term {i} PDF...")
    content = extract_pdf_text(pdf_path)
    if content:
        all_content[f"Term_{i}"] = content
        print(f"Successfully extracted {len(content)} characters from Term {i}")
    else:
        print(f"Failed to extract content from Term {i}")

# Save extracted content to a file
output_file = r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\learn-edu\extracted_content.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

print(f"\nContent saved to {output_file}")
