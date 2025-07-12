import os
from fastapi import APIRouter, Query, HTTPException
from app.services.pdf_extractor import extract_questions_from_pdf

router = APIRouter()

@router.get("/questions")
def extract_pdf_questions(path: str = Query(..., description="Caminho retornado pelo /upload/file")):
    # Debug: confirma se o arquivo existe
    exists = os.path.exists(path)
    print(f"[EXTRACT] Tentando abrir: {path} | existe? {exists}")
    if not exists:
        raise HTTPException(status_code=404, detail=f"Arquivo não encontrado em {path}")
    # Extrai as questões
    questions = extract_questions_from_pdf(path)
    return {"questions": questions}
