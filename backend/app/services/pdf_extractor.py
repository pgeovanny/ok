import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    with pdfplumber.open(pdf_path) as pdf:
        return "".join(page.extract_text() or "" for page in pdf.pages)

def extract_questions_from_pdf(pdf_path: str) -> list[str]:
    text = extract_text_from_pdf(pdf_path)
    parts = text.split("QUESTÃO")
    qs = []
    for idx, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        qs.append(f"QUESTÃO {idx}: {part}")
    return qs
