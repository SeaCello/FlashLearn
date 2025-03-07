# imports for create_flashcards
from django.shortcuts import render
from .models import UserFlashcard
from .forms import CreateCardForm
from gpt.api import generate_flashcards
from gpt.utils import extract_text_from_pdf
import chardet
import docx
from django.contrib.auth.decorators import login_required

# imports for dowload_pdf
from django.http import HttpResponse, JsonResponse
from fpdf import FPDF


@login_required
def create_flashcards(request):
    """
    Processa o arquivo enviado pelo usuário e gera flashcards a partir do seu conteúdo.
    Permite ao usuário editar os flashcards gerados via AJAX.
    
    """
    
    form = CreateCardForm()
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if request.method == 'GET':
        if 'flashcards' in request.session:
            del request.session['flashcards']
        flashcards = []
    
    elif request.method == 'POST':
        
        # Verificar se a requisição é AJAX
        if is_ajax:
            flashcards = process_ajax_edit(request)
            return JsonResponse({
                'status': 'success', 
                'message': 'Flashcards atualizados com sucesso',
            })
        
        # Verificar se o usuário enviou um arquivo
        elif 'file' in request.FILES:
            form = CreateCardForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    # Processar arquivo e gerar flashcards
                    flashcards = process_file_upload(request)
                except Exception as e:
                    form.add_error(None, f"Erro: {str(e)}")
                    print(f"DEBUG - Erro ao gerar flashcards: {str(e)}")
                    flashcards = []
            else:
                flashcards = []
        else:
            flashcards = request.session.get('flashcards', [])

    
    return render(request, 'create_flashcards.html', {
        'form': form,
        'flashcards': flashcards
    })

@login_required
def process_file_upload(request):
    """Processa o upload de arquivo e gera flashcards."""
    file = request.FILES['file']
    
    # Extrair texto do arquivo
    if file.name.lower().endswith('.pdf'): 
        text = extract_text_from_pdf(file)[:6000]
    elif file.name.lower().endswith('.docx'): 
        doc = docx.Document(file)
        text = '\n'.join([p.text for p in doc.paragraphs])[:6000]
    else: 
        raw_content = file.read()
        encoding = chardet.detect(raw_content).get('encoding')
        file.seek(0)
        text = raw_content.decode(encoding)[:6000]
    
    api_flashcards = generate_flashcards(text)
    
    # Salvar no banco e adicionar IDs
    db_flashcards = []
    for data in api_flashcards:
        card = UserFlashcard.objects.create(
            user=request.user,
            title=data['title'],
            content=data['content']
        )
        db_flashcards.append({
            'id': card.id,
            'title': card.title,
            'content': card.content
        })
    
    # Atualizar sessão
    request.session['flashcards'] = db_flashcards
    
    return db_flashcards

@login_required
def process_ajax_edit(request):
    """
    Processa requisições AJAX para criação ou atualização de flashcards.
    Atualiza flashcards existentes se um ID for fornecido ou cria novos flashcards.    
    """
    
    titles = request.POST.getlist('title')
    contents = request.POST.getlist('content')
    flashcard_ids = request.POST.getlist('flashcard_id')
    
    updated_flashcards = []
    
    for i in range(len(titles)):
        if i >= len(contents): 
            continue
            
        title = titles[i]
        content = contents[i]
        
        # Extrair e validar ID
        card_id = None
        if i < len(flashcard_ids) and flashcard_ids[i] and flashcard_ids[i].strip():
            try:
                card_id = int(flashcard_ids[i])
            except (ValueError, TypeError):
                card_id = None
        
        if card_id:
            """ 
            Tenta atualizar o flashcard existente ou cria um novo
            """
            card, _ = UserFlashcard.objects.update_or_create(
                id=card_id, 
                user=request.user,
                defaults={
                    'title': title,
                    'content': content
                }
            )
        else:
            # Se não tiver ID, cria um novo flashcard
            card = UserFlashcard.objects.create(
                user=request.user,
                title=title,
                content=content
            )
        
        updated_flashcards.append({
            'id': card.id,
            'title': card.title,
            'content': card.content
        })
    
    request.session['flashcards'] = updated_flashcards
    
    return updated_flashcards


@login_required
def user_flashcards_home(request):
    """Página inicial do usuário para gestão de flashcards"""
    return render(
        request, 
        'home_user.html',
    )
    

@login_required
def meus_flashcards(request):
    """Exibe os flashcards salvos pelo usuário"""
    user_flashcards = UserFlashcard.objects.filter(user=request.user)
    return render(request, 'meus_flashcards.html', {
        'flashcards': user_flashcards
    })

    
@login_required
def download_pdf(request):
    """
    Recupera os flashcards armazenados no banco de dados do usuário e gera um 
    documento PDF para download.
    Utilizando a biblioteca FPDF, adicionando um título e listando os flashcards.
    Em seguida, retorna o PDF como resposta HTTP para download.
    
    """
    
    # Busca direto do banco de dados
    user_flashcards = UserFlashcard.objects.filter(user=request.user).order_by('-id')[:4]
    
    if not user_flashcards:
        return HttpResponse("Nenhum flashcard encontrado. Crie flashcards antes de fazer o download.", 
                            content_type='text/plain')
        
    try:
        from io import BytesIO 
        buffer_pdf = BytesIO() 
        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, txt="Flashcards Gerados", ln=1, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        for idx, card in enumerate(user_flashcards, 1):
            # Título
            pdf.set_font("Arial", 'B', 12)
            titulo = f"{idx}. {card.title}"
            safe_titulo = titulo.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 10, txt=safe_titulo)
            
            # Conteúdo
            pdf.set_font("Arial", '', 12)
            conteudo = f"{card.content}"
            safe_conteudo = conteudo.encode('latin-1', 'replace').decode('latin-1')
            pdf.multi_cell(0, 10, txt=safe_conteudo)
            
            pdf.ln(5)
        
        pdf_content = pdf.output(dest='S').encode('latin-1')
        buffer_pdf.write(pdf_content)
        buffer_pdf.seek(0)
        
        response = HttpResponse(buffer_pdf.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="flashcards.pdf"'
        return response
    
    except Exception as e:
        return HttpResponse(f"Erro na geração do PDF: {str(e)}", status=500)
