# File: app/routers/questions.py
import os
from fastapi import APIRouter, Query, Body, HTTPException
from app.services.pdf_extractor import extract_questions_from_pdf

router = APIRouter()

def _extract_logic(path: str):
    # Debug: mostra caminho e existência
    exists = os.path.exists(path)
    print(f"[EXTRACT] Tentando abrir: {path} | existe? {exists}")
    if not exists:
        raise HTTPException(status_code=404, detail=f"Arquivo não encontrado em {path}")
    questions = extract_questions_from_pdf(path)
    return {"questions": questions}

# GET — ainda disponível, mas precisa URL-encode correto
@router.get("/extract")
def extract_get(path: str = Query(..., description="Path retornado por /upload/file")):
    return _extract_logic(path)

# POST — evita todo o problema de encoding na URL
@router.post("/extract")
def extract_post(path: str = Body(..., embed=True, description="Use JSON `{ \"path\": \"uploads/arquivo.pdf\" }`")):
    return _extract_logic(path)
