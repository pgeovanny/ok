import pdfplumber

def extract_text_from_pdf(pdf_path: str) -> str:
    print(f"[PDF_EXTRACTOR] Abrindo PDF em: {pdf_path}")
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() or ""
        return full_text

def extract_questions_from_pdf(pdf_path: str) -> list[str]:
    text = extract_text_from_pdf(pdf_path)
    # Exemplo simples: divide onde aparece a palavra "QUESTÃO"
    parts = text.split("QUESTÃO")
    questions = []
    for idx, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
        # re-insere o número da questão se necessário
        questions.append(f"QUESTÃO {idx}: {part}")
    print(f"[PDF_EXTRACTOR] {len(questions)} questões extraídas")
    return questions
