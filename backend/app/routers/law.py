from fastapi import APIRouter, Query, Body
from app.services.pdf_extractor import extract_text_from_pdf
from app.services.openrouter_api import organize_law, apply_pattern

router = APIRouter()

@router.get("/extract")
def extract(path: str = Query(..., description="Caminho retornado por /upload/file")):
    text = extract_text_from_pdf(path)
    return {"law_text": text}

@router.post("/organize")
def organize(law_text: str = Body(..., embed=True), model: str = Body("mistralai/mixtral-8x7b-instruct", embed=True)):
    organized = organize_law(law_text, model=model)
    return {"organized_law": organized}

@router.post("/apply-pattern")
def apply(pattern: str = Body(..., embed=True), organized_law: str = Body(..., embed=True), model: str = Body("mistralai/mixtral-8x7b-instruct", embed=True)):
    result = apply_pattern(pattern, organized_law, model=model)
    return {"schematized": result}