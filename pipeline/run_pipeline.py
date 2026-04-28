from pipeline.ingest import load_pdf
from pipeline.clean import clean_text
from pipeline.chunk import chunk_text
from pipeline.transform import to_structured
import json

def run(file_path):
    pages = load_pdf(file_path)

    all_chunks = []

    for page in pages:
        clean = clean_text(page)
        chunks = chunk_text(clean)
        all_chunks.extend(chunks)

    structured = to_structured(all_chunks)

    with open("output/processed.json", "w") as f:
        json.dump(structured, f, indent=2)

    return structured


if __name__ == "__main__":
    run("data/raw/sample.pdf")
