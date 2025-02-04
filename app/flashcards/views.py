from django.shortcuts import render
from .forms import CreateCardForm
from gpt.utils import extract_text_from_pdf
from gpt.api import generate_flashcards

def create_flashcards(request):
    flashcards = []
    form = CreateCardForm()

    if request.method == 'POST':
        form = CreateCardForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Extrai texto do PDF
                file = request.FILES['file']
                text = extract_text_from_pdf(file)[:6000]  # Limite para 6k tokens
                
                # Gera flashcards usando a API do GPT
                flashcards = generate_flashcards(text)
                
            except Exception as e:
                form.add_error(None, f"Erro: {str(e)}")
    
    return render(request, 'flashcards/create_flashcards.html', {
        'form': form,
        'flashcards': flashcards
    })