import datetime
import os

def format_output(pdf_paths, persona, job, top_sections, top_snippets):
    return {
        "metadata": {
            "input_documents": [os.path.basename(p) for p in pdf_paths],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": "2025-07-26T05:22:26.886027"
        },
        "extracted_sections": [
            {
                "document": s['document'],
                "page_number": s['page_number'],
                "section_title": s['section_title'],
                "importance_rank": s['importance_rank']
            } for s in top_sections
        ],
        "subsection_analysis": [
            {
                "document": s['document'],
                "refined_text": s['refined_text'],
                "page_number": s['page_number']
            } for s in top_snippets
        ]
    }
