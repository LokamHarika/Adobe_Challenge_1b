# Challenge 1b: Multi-Collection PDF Analysis

## Overview
Advanced PDF analysis solution that processes multiple document collections and extracts relevant content based on specific personas and use cases.

## Project Structure
```
Challenge_1b/
├── Collection 1/                    # Travel Planning
│   ├── PDFs/                       # South of France guides
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
├── Collection 2/                    # Adobe Acrobat Learning
│   ├── PDFs/                       # Acrobat tutorials
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
├── Collection 3/                    # Recipe Collection
│   ├── PDFs/                       # Cooking guides
│   ├── challenge1b_input.json      # Input configuration
│   └── challenge1b_output.json     # Analysis results
└── README.md
```

## Collections

### Collection 1: Travel Planning
- **Challenge ID**: round_1b_002
- **Persona**: Travel Planner
- **Task**: Plan a 4-day trip for 10 college friends to South of France
- **Documents**: 7 travel guides

### Collection 2: Adobe Acrobat Learning
- **Challenge ID**: round_1b_003
- **Persona**: HR Professional
- **Task**: Create and manage fillable forms for onboarding and compliance
- **Documents**: 15 Acrobat guides

### Collection 3: Recipe Collection
- **Challenge ID**: round_1b_001
- **Persona**: Food Contractor
- **Task**: Prepare vegetarian buffet-style dinner menu for corporate gathering
- **Documents**: 9 cooking guides

## Input/Output Format

### Input JSON Structure
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [{"filename": "doc.pdf", "title": "Title"}],
  "persona": {"role": "User Persona"},
  "job_to_be_done": {"task": "Use case description"}
}
```

### Output JSON Structure
```json
{
  "metadata": {
    "input_documents": ["list"],
    "persona": "User Persona",
    "job_to_be_done": "Task description"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Content",
      "page_number": 1
    }
  ]
}
```

## Key Features
- Persona-based content analysis
- Importance ranking of extracted sections
- Multi-collection document processing
- Structured JSON output with metadata

## Technologies & Modules Used

1. main.py
   - Driver script to coordinate all stages: parsing, embedding, scoring, formatting.

2. utils/pdf_utils.py
   - Parses PDF documents using PyMuPDF (fitz).
   - Extracts structured headings and paragraphs.
   - Keeps track of source document and page number.

3. utils/embedding_utils.py
   - Generates embeddings using sentence-transformers (e.g., MiniLM).
   - Computes cosine similarity between user intent and document paragraphs.

4. utils/output_formatter.py
   - Ranks and selects top 5 relevant sections.
   - Formats them into a JSON-compliant output.

## How to Run

1. Install dependencies
   pip install -r requirements.txt

2. Run the pipeline
   python main.py

This processes the PDFs and input persona to generate the structured output JSON.

## 📚 Extending to Collection 2 and 3

To run for Collection 2 or Collection 3:
- Replace the PDFs/ and JSON files in the root folder, or
- Duplicate the structure for each collection, e.g., Collection 2/, Collection 3/
- Ensure main.py points to the correct collection paths

Each collection is processed independently but using the same pipeline.

## 💡 Why These Tools?

Component             | Reason
----------------------|---------------------------------------------------------------
PyMuPDF (fitz)        | Lightweight PDF parsing + layout-aware text extraction
SentenceTransformers  | Efficient semantic understanding for embeddings (MiniLM, etc.)
Cosine Similarity     | Fast and interpretable ranking of paragraph relevance
JSON                  | Simple and structured format for challenge output

## ⏱ Performance

- ⌛ Inference Time: < 60s (CPU only)
- 📦 Model Size: < 1GB (MiniLM or equivalent)
- 🔍 Output Quality: Relevant, ranked, and readable

## 👤 Authors

- Team Name: Learnova
- Challenge: Adobe Document Intelligence – Round 1B

