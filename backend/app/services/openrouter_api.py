import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_openrouter(prompt: str, model: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Você é um especialista em concursos e legislação."},
            {"role": "user", "content": prompt}
        ]
    }
    r = requests.post(BASE_URL, headers=headers, json=payload, timeout=90)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def organize_questions(raw: str, model: str) -> str:
    prompt = (
        "O texto abaixo contém questões de concurso extraídas de PDF, mas está desorganizado."
        " Organize cada questão numerando, destacando enunciado, alternativas e gabarito.\n\n" + raw
    )
    return ask_openrouter(prompt, model)

def learn_pattern(organized: str, model: str) -> str:
    prompt = (
        "Analise as questões abaixo e identifique o padrão de cobrança da banca."
        " Ao finalizar, responda apenas 'Padrão da banca aprendido:' seguido do padrão.\n\n" + organized
    )
    return ask_openrouter(prompt, model)

def organize_law(law_text: str, model: str) -> str:
    prompt = (
        "Organize o texto da lei abaixo em tópicos e quadros para facilitar a esquematização posterior.\n\n" + law_text
    )
    return ask_openrouter(prompt, model)

def apply_pattern(pattern: str, organized_law: str, model: str) -> str:
    prompt = (
        "Com base no padrão a seguir e na lei organizada, aplique a esquematização com quadros, tabelas, grifos verdes para pontos fortes e vermelhos para pontos fracos.\n\n" +
        f"PADRÃO:\n{pattern}\n\nLEI ORGANIZADA:\n{organized_law}"
    )
    return ask_openrouter(prompt, model)
