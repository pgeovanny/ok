import requests
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_openrouter(prompt, model="mistralai/mixtral-8x7b-instruct"):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }
    r = requests.post(OPENROUTER_API_URL, headers=headers, json=data)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]

def organize_questions_with_ia(questoes, model="mistralai/mixtral-8x7b-instruct"):
    prompt = (
        "Organize as questões abaixo em uma lista limpa, separando enunciado, alternativas e gabarito, para facilitar análise:\n\n"
        + "\n\n".join(questoes)
    )
    return ask_openrouter(prompt, model=model)
