from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import mimetypes

from .models import Document  # Importando nosso modelo Document

@csrf_exempt
def upload_document(request):
    """
    View responsável por receber o upload de um arquivo e salvá-lo no banco de dados.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'No file uploaded'}, status=400)
    
    file = request.FILES['file']
    
    # Validação do formato do arquivo
    # Os formatos permitidos para o upload são .txt, .docx e .pdf
    allowed_formats = ['.txt', '.docx', '.pdf']
    file_extension = os.path.splitext(file.name)[1].lower()
    
    if file_extension not in allowed_formats:
        return JsonResponse({
            'error': f'Invalid file format. Allowed formats: {", ".join(allowed_formats)}'
        }, status=400)
    
    # Validação do tamanho do arquivo
    # O tamanho máximo permitido para o upload é de 5MB
    if file.size > settings.MAX_UPLOAD_SIZE:
        return JsonResponse({
            'error': f'File too large. Maximum size is {settings.MAX_UPLOAD_SIZE/1024/1024}MB'
        }, status=400)
    
    try:
        # Salvar o documento
        document = Document.objects.create(file=file)
        
        # Chamar a API da OpenAI para processar o documento
        # TODO: Implementar essa lógica
        with open(f'media/outputs/{document.id}.txt', 'w') as f:
            f.write("Exemplo de output processado")
        
        document.output_file = f'outputs/{document.id}.txt'
        document.processed = True
        document.save()
        
        return JsonResponse({
            'message': 'Document uploaded successfully',
            'document_id': str(document.id)
        })
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def download_document(request, document_id):
    try:
        # Tentamos buscar o documento pelo ID
        document = Document.objects.get(id=document_id)
        
        # Verificamos se o documento já foi processado
        if not document.processed or not document.output_file:
            return JsonResponse({'error': 'Document not processed yet'}, status=404)
        
        # Construímos o caminho completo do arquivo
        file_path = os.path.join(settings.MEDIA_ROOT, str(document.output_file))
        
        # Verificamos se o arquivo existe no sistema de arquivos
        if not os.path.exists(file_path):
            return JsonResponse({'error': 'Output file not found'}, status=404)
        
        # Determinamos o tipo do arquivo
        content_type, _ = mimetypes.guess_type(file_path)
        if content_type is None:
            content_type = 'application/octet-stream'
        
        # Preparamos a resposta com o arquivo
        response = FileResponse(open(file_path, 'rb'), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
        
        return response
        
    except Document.DoesNotExist:
        # Caso o documento não seja encontrado no banco de dados
        return JsonResponse({'error': 'Document not found'}, status=404)
    except Exception as e:
        # Para qualquer outro erro que possa ocorrer
        return JsonResponse({'error': str(e)}, status=500)