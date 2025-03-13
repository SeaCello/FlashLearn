from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from fpdf import FPDF
from django.contrib.auth.decorators import login_required
from .services import FlashcardService, PDFService
from .models import UserFlashcard
from .forms import CreateCardForm



@login_required
def create_flashcards(request):
    """
    Processes the file uploaded by the user and generates flashcards from its content.
    Allows the user to edit the generated flashcards via AJAX.
    Handles both GET and POST requests:
    - GET: Clears any existing flashcards in the session.
    - POST: 
        - If the request is an AJAX request, updates the flashcards with the provided titles, contents, and IDs.
        - If a file is uploaded, validates the form and generates flashcards from the file content.
        - If no file is uploaded, retrieves flashcards from the session.
    """

    form = CreateCardForm()
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    if request.method == 'GET':
        if 'flashcards' in request.session:
            del request.session['flashcards']
        flashcards = []
    
    elif request.method == 'POST':
        
        if is_ajax:
            titles = request.POST.getlist('title')
            contents = request.POST.getlist('content')
            flashcard_ids = request.POST.getlist('flashcard_id')
            flashcards = FlashcardService.update_flashcards_from_data(request.user, titles, contents, flashcard_ids)
            request.session['flashcards'] = flashcards
            return JsonResponse({
                'status': 'success', 
                'message': 'Flashcards atualizados com sucesso',
            })
        
        elif 'file' in request.FILES:
            form = CreateCardForm(request.POST, request.FILES)
            if form.is_valid():
                try:
                    flashcards = FlashcardService.create_flashcards_from_file(
                                                request.user, request.FILES['file'])
                    request.session['flashcards'] = flashcards
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
def user_flashcards_home(request):
    """
    User's home page for flashcard management.
    """
    
    return render(
        request, 
        'home_user.html',
    )
    

@login_required
def meus_flashcards(request):
    """
    Displays the flashcards saved by the user.
    """
    
    user_flashcards = UserFlashcard.objects.filter(user=request.user)
    return render(request, 'meus_flashcards.html', {
        'flashcards': user_flashcards
    })

    
@login_required
def download_pdf(request):
    """
    Generates a PDF containing the user's flashcards for download.
    
    This view retrieves the latest 4 flashcards created by the user, generates a PDF
    document with these flashcards, and returns it as a downloadable file.
    
    If no flashcards are found for the user, an appropriate message is returned.
    """
    
    user_flashcards = UserFlashcard.objects.filter(user=request.user).order_by('-id')[:4]
    
    if not user_flashcards:
        return HttpResponse("Nenhum flashcard encontrado. Crie flashcards antes de fazer o download.", 
                        content_type='text/plain')
    
    try:
        buffer_pdf = PDFService.generate_flashcards_pdf(user_flashcards)
        
        response = HttpResponse(buffer_pdf.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="flashcards.pdf"'
        return response
    
    except Exception as e:
        return HttpResponse(f"Erro na geração do PDF: {str(e)}", status=500)