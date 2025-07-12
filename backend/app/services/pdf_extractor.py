import pdfplumber

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_questions_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    # Aqui, adapte para separar questões conforme o padrão do seu PDF.
    # Exemplo: cada questão começa com 'QUESTÃO'
    questoes = [q.strip() for q in text.split("QUESTÃO") if q.strip()]
    return questoes[:50]  # Limite de 50 questões
