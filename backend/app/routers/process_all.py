from fastapi import APIRouter, Body
from app.services.openrouter_api import analyze_pattern, organize_law_text, esquematize_law

router = APIRouter()

@router.post("/analyze/pattern")
def analyze_pattern_endpoint(questions: str = Body(...), model: str = "mistralai/mistral-8x7b-instruct"):
    result = analyze_pattern(questions, model=model)
    return {"message": result}

@router.post("/organize/law")
def organize_law_endpoint(law_text: str = Body(...), model: str = "mistralai/mistral-8x7b-instruct"):
    organized = organize_law_text(law_text, model=model)
    return {"preview": organized}

@router.post("/esquematize")
def esquematize_law_endpoint(pattern: str = Body(...), law_organized: str = Body(...), model: str = "mistralai/mistral-8x7b-instruct"):
    esquematizado = esquematize_law(pattern, law_organized, model=model)
    return {"output": esquematizado}
