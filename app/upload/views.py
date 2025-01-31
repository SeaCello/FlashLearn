from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Upload
from .forms import UploadForm

# Create your views here.
class UploadView(CreateView):
    model = Upload
    form_class = UploadForm
    success_url = reverse_lazy('upload')  # Redireciona para a mesma página após o sucesso    

