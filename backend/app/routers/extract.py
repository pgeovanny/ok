from fastapi import APIRouter, Query
from app.services.pdf_extractor import extract_questions_from_pdf, extract_text_from_pdf

router = APIRouter()

@router.get("/extract/questions")
def extract_pdf_questions(path: str = Query(...)):
    questions = extract_questions_from_pdf(path)
    return {"questions": questions}

@router.get("/extract/lawtext")
def extract_pdf_law(path: str = Query(...)):
    law_text = extract_text_from_pdf(path)
    return {"law_text": law_text}
