import requests
import os

OPENROUTER_KEY = os.getenv("OPENROUTER_KEY")

def ask_openrouter(prompt, model="mistralai/mistral-8x7b-instruct"):
    # igual já usamos antes
    ...

def analyze_pattern(questions, model):
    prompt = f"""Analise cuidadosamente as questões abaixo e identifique o padrão da banca. Ao terminar, responda apenas: 'Padrão da banca entendido.'
QUESTÕES:
{questions}
"""
    return ask_openrouter(prompt, model=model)

def organize_law_text(law_text, model):
    prompt = f"""Organize o texto a seguir em tópicos, artigos, quadros, destaques de informações importantes para facilitar a esquematização posterior:
TEXTO DA LEI:
{law_text}
"""
    return ask_openrouter(prompt, model=model)

def esquematize_law(pattern, law_organized, model):
    prompt = f"""Com base no padrão abaixo, aplique a esquematização na lei organizada, usando tabelas, quadros, grifos verdes para acertos, vermelhos para erros e o layout do app:
PADRÃO:
{pattern}
LEI ORGANIZADA:
{law_organized}
"""
    return ask_openrouter(prompt, model=model)
