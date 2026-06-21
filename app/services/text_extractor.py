# app/services/text_extractor.py

import fitz  # PyMuPDF


def extract_text(file_path: str) -> str:
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            text += page.get_text()

        return text

    raise ValueError("Unsupported file format")