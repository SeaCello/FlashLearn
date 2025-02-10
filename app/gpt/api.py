import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_flashcards(text):
    """
    Gera flashcards a partir de um texto usando a API do GPT.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "Gere 4 resumos curtos (máximo 50 palavras cada) para flashcards. Formato: lista com '-'"},
                {"role": "user", "content": f"Texto:\n{text}\n\nResumos:"}
            ],
            temperature=0.7
        )
        
        # Processa a resposta
        raw_content = response.choices[0].message.content
        flashcards = [line.replace('-', '').strip() 
                    for line in raw_content.split('\n') 
                    if line.strip()][:4]
        
        return flashcards
    except Exception as e:
        raise Exception(f"Erro ao gerar flashcards: {str(e)}")