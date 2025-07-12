from fastapi import APIRouter, Query
from app.services.pdf_extractor import extract_questions_from_pdf

router = APIRouter()

@router.get("/extract/questions")
def extract_pdf_questions(path: str = Query(..., description="Path do arquivo PDF")):
    print(f"[EXTRACT] Tentando abrir o arquivo em: {path}")
    questions = extract_questions_from_pdf(path)
    return {"questions": questions}
