import pdfplumber

def extract_text_from_pdf(pdf_path):
    print(f"[PDF_EXTRACTOR] Abrindo PDF em: {pdf_path}")
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        return text

def extract_questions_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    # Simples: divide por 'QUESTÃO' se quiser testar
    questions = [q.strip() for q in text.split('QUESTÃO') if q.strip()]
    print(f"[PDF_EXTRACTOR] {len(questions)} questões extraídas")
    return questions
