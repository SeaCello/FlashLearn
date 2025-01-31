from django import forms
from .models import Upload

MAX_SIZE = 5 * 1024 * 1024
ALLOWED_EXTENSIONS = ['.txt', '.docx', '.pdf']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            if file.size > MAX_SIZE:
                raise forms.ValidationError("O arquivo não pode ser maior que 5 MB.")
            if not any(file.name.endswith(ext) for ext in ALLOWED_EXTENSIONS):
                raise forms.ValidationError("Somente arquivos .txt, .docx e .pdf são permitidos.")
        return file
    