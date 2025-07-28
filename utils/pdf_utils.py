import fitz
import re
import os

def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        pages.append({ "page": i + 1, "text": text })
    return pages

def extract_sections(pages):
    sections = []
    pattern = re.compile(r'^(\d+(\.\d+)*)(\s+|-)(.+)', re.MULTILINE)
    for page in pages:
        page_number = page['page']
        lines = page['text'].split('\n')
        for i, line in enumerate(lines):
            if pattern.match(line.strip()) or len(line.strip()) > 40:
                section_title = line.strip()
                section_text = '\n'.join(lines[i:i+6])
                sections.append({
                    "title": section_title,
                    "page": page_number,
                    "text": section_text
                })
    return sections

def extract_from_pdfs(pdf_paths):
    all_sections = []
    for path in pdf_paths:
        pages = extract_text_by_page(path)
        sections = extract_sections(pages)
        for s in sections:
            s["document"] = os.path.basename(path)
        all_sections.extend(sections)
    return all_sections
