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

def analyze_content_structure(text):
    """Analyze the content structure to identify chapters and topics"""
    content_structure = {
        "chapters": [],
        "topics": []
    }
    
    # Find chapter titles and page numbers
    chapter_pattern = r'UNIT\s+(\d+)\s+([^\n]+)'
    chapters = re.findall(chapter_pattern, text)
    
    for chapter_num, chapter_title in chapters:
        content_structure["chapters"].append({
            "number": int(chapter_num),
            "title": chapter_title.strip()
        })
    
    # Find topic patterns (like 1.1, 2.1, etc.)
    topic_pattern = r'(\d+\.\d+)\s+([^\n]+)'
    topics = re.findall(topic_pattern, text)
    
    for topic_num, topic_title in topics:
        content_structure["topics"].append({
            "number": topic_num,
            "title": topic_title.strip()
        })
    
    return content_structure

# Path to the Class 5 PDF files
pdf_paths = [
    r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\Learning edu\Tn sylubus\Class_5_Mathematics_English_Medium-Term_1-2024_Edition-www.tntextbooks.in.pdf",
    r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\Learning edu\Tn sylubus\Class_5_Mathematics_English_Medium-Term_2-2024_Edition-www.tntextbooks.in.pdf"
]

# Extract and analyze content from all PDFs
all_content = {}
all_analysis = {}
for i, pdf_path in enumerate(pdf_paths, 1):
    print(f"Extracting content from Class 5 Term {i} PDF...")
    content = extract_pdf_text(pdf_path)
    if content:
        all_content[f"Term_{i}"] = content
        analysis = analyze_content_structure(content)
        all_analysis[f"Term_{i}"] = analysis
        print(f"Successfully extracted {len(content)} characters from Term {i}")
        print(f"Found {len(analysis['chapters'])} chapters and {len(analysis['topics'])} topics in Term {i}")
    else:
        print(f"Failed to extract content from Term {i}")

# Save extracted content to files
content_output_file = r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\learn-edu\class5_extracted_content.json"
with open(content_output_file, 'w', encoding='utf-8') as f:
    json.dump(all_content, f, ensure_ascii=False, indent=2)

analysis_output_file = r"c:\Users\thira\OneDrive - Rathinam Group Of Institutions\Desktop\My carrier\projects\learn-edu\class5_content_analysis.json"
with open(analysis_output_file, 'w', encoding='utf-8') as f:
    json.dump(all_analysis, f, ensure_ascii=False, indent=2)

print(f"\nContent saved to {content_output_file}")
print(f"Analysis saved to {analysis_output_file}")

# Print summary
for term, analysis in all_analysis.items():
    print(f"\n{term}:")
    print("Chapters:")
    for chapter in analysis["chapters"]:
        print(f"  {chapter['number']}. {chapter['title']}")
    
    print("Topics:")
    for topic in analysis["topics"][:10]:  # Show first 10 topics
        print(f"  {topic['number']}. {topic['title']}")
    if len(analysis["topics"]) > 10:
        print(f"  ... and {len(analysis['topics']) - 10} more topics")