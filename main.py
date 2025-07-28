import json, os
from utils.pdf_utils import extract_from_pdfs
from utils.embedding_utils import rank_sections_and_snippets
from utils.output_formatter import format_output

if __name__ == "__main__":
    with open("challenge1b_input.json", "r") as f:
        input_data = json.load(f)

    persona = input_data["persona"]["role"]
    job = input_data["job_to_be_done"]["task"]
    pdf_paths = [os.path.join("PDFs", doc["filename"]) for doc in input_data["documents"]]

    sections = extract_from_pdfs(pdf_paths)
    top_sections, top_snippets = rank_sections_and_snippets(sections, persona, job)

    output_json = format_output(pdf_paths, persona, job, top_sections, top_snippets)

    with open("challenge1b_output.json", "w") as f:
        json.dump(output_json, f, indent=2)

    print("✅ challenge1b_output.json generated successfully.")
