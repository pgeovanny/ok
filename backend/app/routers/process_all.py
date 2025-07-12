from fastapi import APIRouter, Request
from app.services.openrouter_api import ask_openrouter, organize_questions_with_ia
from app.services.pdf_extractor import extract_questions_from_pdf
from app.services.templates import gerar_html_template
from weasyprint import HTML

router = APIRouter()

@router.post("/process-all/")
async def process_all(request: Request):
    data = await request.json()
    pdf_path = data["pdf_path"]
    modelo_ia = data.get("model", "mistralai/mixtral-8x7b-instruct")

    # 1. Extrai as questões (limite de 50)
    questoes = extract_questions_from_pdf(pdf_path)
    questoes_limitadas = questoes[:50] if isinstance(questoes, list) else questoes

    # 2. Organiza via IA
    questoes_organizadas = organize_questions_with_ia(questoes_limitadas, model=modelo_ia)

    # 3. Gera HTML
    html = gerar_html_template(questoes_organizadas)

    # 4. Exporta PDF via WeasyPrint
    output_pdf = pdf_path.replace(".pdf", "_resumo.pdf")
    HTML(string=html).write_pdf(output_pdf)

    return {"resumo_pdf": output_pdf}
