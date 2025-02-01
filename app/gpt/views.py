import fitz  # PyMuPDF
import os
from django.shortcuts import render
from openai import OpenAI
from .forms import FlashcardForm

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def flashcard_view(request):
    flashcards = []
    form = FlashcardForm()

    if request.method == 'POST':
        form = FlashcardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Extrai texto
                file = request.FILES['file']
                text = extract_text_from_pdf(file)[:6000]  # Limite para 6k tokens
                
                # Gera flashcards
                response = client.chat.completions.create(
                    model="gpt-4-turbo",
                    messages=[
                        {"role": "system", "content": "Gere 4 resumos curtos (máximo 50 palavras cada) para flashcards. Formato: lista com '-'"},
                        {"role": "user", "content": f"Texto:\n{text}\n\nResumos:"}
                    ],
                    temperature=0.7
                )
                
                # Processa resposta
                raw_content = response.choices[0].message.content
                flashcards = [line.replace('-', '').strip() 
                            for line in raw_content.split('\n') 
                            if line.strip()][:4]
                
            except Exception as e:
                form.add_error(None, f"Erro: {str(e)}")
    
    return render(request, 'gpt/flashcards.html', {
        'form': form,
        'flashcards': flashcards
    })