from fastapi import APIRouter, Query, Body
from app.services.pdf_extractor import extract_questions_from_pdf
from app.services.openrouter_api import organize_questions, learn_pattern

router = APIRouter()

@router.get("/extract")
def extract(path: str = Query(..., description="Caminho retornado por /upload/file")):
    qs = extract_questions_from_pdf(path)
    return {"questions": qs}

@router.post("/organize")
def organize(qs: list[str] = Body(..., embed=True), model: str = Body("mistralai/mixtral-8x7b-instruct", embed=True)):
    joined = "\n".join(qs)
    organized = organize_questions(joined, model=model)
    return {"organized": organized}

@router.post("/learn")
def learn(organized: str = Body(..., embed=True), model: str = Body("mistralai/mixtral-8x7b-instruct", embed=True)):
    pattern = learn_pattern(organized, model=model)
    return {"pattern": pattern}