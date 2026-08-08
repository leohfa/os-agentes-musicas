import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()  # carrega as variáveis do .env

MINHA_CHAVE = os.environ.get("GEMINI_API_KEY")

if not MINHA_CHAVE:
    raise ValueError("Chave não encontrada. Verifique se o arquivo .env existe e contém GEMINI_API_KEY.")

client = genai.Client(api_key=MINHA_CHAVE)
config = types.GenerateContentConfig(
    system_instruction=(
        "Voce e um Assistente Pessoal de Produtividade super organizado e motivador. "
        "Seu objetivo e ajudar o usuario a planejar o dia dele, definir metas claras e vencer a procrastinacao. "
        "Responda sempre em portugues de forma clara e estruturada."
    ),
    temperature=0.7,
)

print("\n--- ASSISTENTE PESSOAL ATIVADO ---")
print("Digite sua mensagem abaixo (ou digite 'sair' para encerrar).\n")

while True:
    pergunta_usuario = input("Voce: ")

    if pergunta_usuario.lower() == 'sair':
        print("\nAssistente: Ate logo! Bons estudos!")
        break

    print("\n[Pensando...]")

    resposta = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=pergunta_usuario,
        config=config,
    )

    print(f"\nAssistente: {resposta.text}\n")
