# imports for create_flashcards
from django.shortcuts import render
from .forms import CreateCardForm
from gpt.api import generate_flashcards
from gpt.utils import extract_text_from_pdf
import chardet
import docx

# imports for dowload_pdf
from django.http import HttpResponse
from fpdf import FPDF

def create_flashcards(request):
    """
    Processa o arquivo enviado pelo usuário e gera flashcards a partir do seu conteúdo.
    
    Este método verifica a extensão do arquivo:
    - Se for DOCX, utiliza a biblioteca 'docx' para extrair os parágrafos.
    - Se for TXT, detecta a codificação com 'chardet' e decodifica o conteúdo.
    - Se for PDF, utiliza a função extract_text_from_pdf() para extrair o texto.
    
    Em seguida, chama a função generate_flashcards() para criar os flashcards,
    armazena-os na sessão do usuário e exibe a página de criação com os flashcards.
    """
    
    flashcards = []
    form = CreateCardForm()

    if request.method == 'POST':
        form = CreateCardForm(request.POST, request.FILES)
        
        if form.is_valid():
            try:
                file = request.FILES['file'] 
                #process PDF
                if file.name.lower().endswith('.pdf'):
                    text = extract_text_from_pdf(file)[:6000]  
                
                #process DOCX
                elif file.name.lower().endswith('.docx'):
                    doc = docx.Document(file)
                    text = '\n'.join([p.text for p in doc.paragraphs])[:6000]
                
                #process TXT
                else:
                    encoding = chardet.detect(file.read())['encoding']
                    file.seek(0)
                    text = file.read().decode(encoding)[:6000]

                
                flashcards = generate_flashcards(text)
                request.session['flashcards'] = flashcards 


            except Exception as e:
                form.add_error(None, f"Erro: {str(e)}")
    
    return render(request, 'flashcards/create_flashcards.html', {
        'form': form,
        'flashcards': flashcards
    })
    
    
    
def download_pdf(request):
    """
    Recupera os flashcards armazenados na sessão do usuário e gera um documento PDF para download.
    
    O método verifica se existem flashcards na sessão. Se existirem, cria um PDF
    utilizando a biblioteca FPDF, adicionando um título e listando os flashcards.
    Em seguida, retorna o PDF como resposta HTTP para download.
    """
    
    flashcards = request.session.get('flashcards', [])
    
    if not flashcards:
        return HttpResponse("Nenhum flashcard encontrado.", content_type='text/plain')

    try:
        from io import BytesIO 
        # o pdf corrompe se não for feito isso
        buffer_pdf = BytesIO() 
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, txt="Flashcards Gerados", ln=1, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        for idx, card in enumerate(flashcards, 1):
            texto = f"{idx}. {card}"
            safe_text = texto.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 10, txt=safe_text)
            pdf.ln(8)

        pdf.output(buffer_pdf, 'F') 
        buffer_pdf.seek(0)
        response = HttpResponse(buffer_pdf.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="flashcards.pdf"'
        return response
    
    except Exception as e:
        return HttpResponse(f"Erro na geração do PDF: {str(e)}", status=500)