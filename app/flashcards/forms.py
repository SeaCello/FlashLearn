from django import forms

class CreateCardForm(forms.Form):
    file = forms.FileField(
        label='',
        widget=forms.ClearableFileInput(attrs={'class': 'w-full text-gray-400 font-semibold text-sm bg-white border file:cursor-pointer cursor-pointer file:border-0 file:py-3 file:px-4 file:mr-4 file:bg-gray-100 file:hover:bg-gray-200 file:text-gray-500 rounded'}),
    )
    
    def clean_file(self):
        file = self.cleaned_data['file']
        if file.size > 5*1024*1024:
            raise forms.ValidationError("Arquivo muito grande (máximo 5MB)")
        if not file.name.lower().endswith(('.pdf', '.docx', '.txt')):
            raise forms.ValidationError("Formato não suportado")
        return file