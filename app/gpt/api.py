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
        {
            "role": "system",
            "content": """Você é um especialista em criar flashcards concisos e diretos. Para cada flashcard:
                - Mantenha o formato simples: uma frase direta por flashcard
                - Evite usar marcadores ou subtópicos dentro do flashcard
                - Limite cada flashcard a uma única ideia principal
                - Use no máximo 50 palavras por flashcard
                - Limite cada flashcard a uma única ideia principal
                - Use linguagem simples e direta
                - Formato: 'Pergunta | Resposta'
                - Comece cada flashcard com '- '"""
        },
        {
            "role": "user",
            "content": f"""Analise o texto a seguir e crie 4 flashcards.
            Cada flashcard deve ter uma pergunta como título e uma resposta:
:

            Texto:
            {text}"""
        }
        ],
            temperature=0.7,
            max_tokens=1000,
            presence_penalty=0.2,
            frequency_penalty=0.3
        )


        raw_content = response.choices[0].message.content
        flashcards_raw = [line.replace('-', '').strip() 
                        for line in raw_content.split('\n') 
                        if line.strip()][:4]
        
        # Separa título e conteúdo
        flashcards = []
        for card in flashcards_raw:
            parts = card.split('|')
            if len(parts) == 2:
                flashcards.append({
                    'title': parts[0].strip(),
                    'content': parts[1].strip()
                })
            else:
                flashcards.append({
                    'title': 'Flashcard',
                    'content': card
                })
        

        return flashcards
    
    except Exception as e:
        raise Exception(f"Erro ao gerar flashcards: {str(e)}")