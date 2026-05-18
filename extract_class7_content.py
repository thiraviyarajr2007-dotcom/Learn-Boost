#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 7 Mathematics PDF Content Extractor - TN State Board
Extracts and analyzes content from Term 1, 2, and 3 textbooks
"""

import json
import re
import os
from pathlib import Path

def extract_pdf_content(pdf_path):
    """Extract text content from PDF file"""
    try:
        import PyPDF2
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text_content = ""
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text_content += page.extract_text() + "\n"
                
        return text_content
        
    except ImportError:
        print("PyPDF2 not installed. Using alternative method...")
        return None
    except Exception as e:
        print(f"Error extracting from {pdf_path}: {e}")
        return None

def analyze_content_structure(text_content, term_name):
    """Analyze the extracted content to identify chapters and topics"""
    
    chapters = []
    topics = []
    
    # Common chapter patterns in TN textbooks
    chapter_patterns = [
        r'(\d+)\s*[\.]\s*([A-Z][A-Z\s]+)',  # "1. NUMBER SYSTEM"
        r'CHAPTER\s*(\d+)\s*[:\-]?\s*([A-Z][A-Z\s]+)',  # "CHAPTER 1: NUMBER SYSTEM"
        r'(\d+)\s+([A-Z][A-Z\s]+)',  # "1 NUMBER SYSTEM"
    ]
    
    # Topic patterns
    topic_patterns = [
        r'(\d+\.\d+)\s*([A-Za-z][A-Za-z\s\(\)]+)',  # "1.1 Introduction"
        r'(\d+\.\d+)\s*([A-Za-z][A-Za-z\s]+)',  # "1.1 Introduction"
        r'([A-Za-z]+\s*\d+\.\d+)\s*([A-Za-z][A-Za-z\s]+)',  # "Exercise 1.1"
    ]
    
    lines = text_content.split('\n')
    
    for line in lines:
        line = line.strip()
        if len(line) < 3:  # Skip very short lines
            continue
            
        # Check for chapter titles
        for pattern in chapter_patterns:
            match = re.match(pattern, line.upper())
            if match:
                chapter_num = match.group(1)
                chapter_title = match.group(2).strip()
                if len(chapter_title) > 5:  # Filter out short matches
                    chapters.append({
                        "number": chapter_num,
                        "title": chapter_title
                    })
                break
        
        # Check for topics
        for pattern in topic_patterns:
            match = re.match(pattern, line)
            if match:
                topic_num = match.group(1)
                topic_title = match.group(2).strip()
                if len(topic_title) > 3:  # Filter out short matches
                    topics.append({
                        "number": topic_num,
                        "title": topic_title
                    })
                break
    
    return {
        "term": term_name,
        "chapters": chapters,
        "topics": topics,
        "total_content_length": len(text_content),
        "content_preview": text_content[:500] + "..." if len(text_content) > 500 else text_content
    }

def extract_class7_content():
    """Extract content from all Class 7 Mathematics textbooks"""
    
    # Define the PDF paths
    base_path = Path("c:/Users/thira/OneDrive - Rathinam Group Of Institutions/Desktop/My carrier/projects/Learning edu/Tn sylubus")
    
    pdf_files = {
        "Term_1": "Class_7_Mathematics_English_Medium-Term_1-2024_Edition-www.tntextbooks.in (1) (1).pdf",
        "Term_2": "Class_7_Mathematics_English_Medium-Term_2-2024_Edition-www.tntextbooks.in.pdf", 
        "Term_3": "Class_7_Mathematics_English_Medium-Term_3-2024_Edition-www.tntextbooks.in.pdf"
    }
    
    analysis_results = {}
    
    for term, filename in pdf_files.items():
        pdf_path = base_path / filename
        
        print(f"\n=== Processing {term} ===")
        print(f"File: {filename}")
        
        if not pdf_path.exists():
            print(f"❌ File not found: {pdf_path}")
            analysis_results[term] = {
                "term": term,
                "chapters": [],
                "topics": [],
                "total_content_length": 0,
                "content_preview": "File not found",
                "error": "File not found"
            }
            continue
        
        # Extract content
        text_content = extract_pdf_content(str(pdf_path))
        
        if text_content:
            print(f"+ Successfully extracted content")
            print(f"Content length: {len(text_content)} characters")
            
            # Analyze structure
            analysis = analyze_content_structure(text_content, term)
            analysis_results[term] = analysis
            
            print(f"* Found {len(analysis['chapters'])} chapters")
            print(f"* Found {len(analysis['topics'])} topics")
            
            # Show first few chapters and topics
            if analysis['chapters']:
                print("\nFirst few chapters:")
                for i, chapter in enumerate(analysis['chapters'][:3]):
                    print(f"  {chapter['number']}. {chapter['title']}")
            
            if analysis['topics']:
                print("\nFirst few topics:")
                for i, topic in enumerate(analysis['topics'][:5]):
                    print(f"  {topic['number']} {topic['title']}")
        else:
            print(f"X Failed to extract content")
            analysis_results[term] = {
                "term": term,
                "chapters": [],
                "topics": [],
                "total_content_length": 0,
                "content_preview": "Extraction failed",
                "error": "Content extraction failed"
            }
    
    # Save analysis results
    output_file = "class7_content_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n* Analysis saved to: {output_file}")
    
    # Print summary
    print(f"\n=== SUMMARY ===")
    total_chapters = sum(len(result['chapters']) for result in analysis_results.values())
    total_topics = sum(len(result['topics']) for result in analysis_results.values())
    total_content = sum(result['total_content_length'] for result in analysis_results.values())
    
    print(f"Total Chapters: {total_chapters}")
    print(f"Total Topics: {total_topics}")
    print(f"Total Content: {total_content:,} characters")
    
    return analysis_results

if __name__ == "__main__":
    results = extract_class7_content()