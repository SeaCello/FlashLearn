from django import forms

class FlashcardForm(forms.Form):
    file = forms.FileField(
        label='Selecione um arquivo',
    )
    
    def clean_file(self):
        file = self.cleaned_data['file']
        if file.size > 5*1024*1024:
            raise forms.ValidationError("Arquivo muito grande (máximo 5MB)")
        if not file.name.lower().endswith(('.pdf', '.docx', '.txt')):
            raise forms.ValidationError("Formato não suportado")
        return file
    