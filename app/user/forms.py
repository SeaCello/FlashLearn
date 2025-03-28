from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Div

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Nome de usuário',
        widget=forms.TextInput(attrs={'placeholder': 'Digite seu nome de usuário'}),
        error_messages={
            'required': 'O nome de usuário é obrigatório',
            'unique': 'Este nome de usuário já está em uso'
        }
    )
    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'placeholder': 'Digite seu e-mail'}),
        error_messages={
            'required': 'O e-mail é obrigatório',
            'invalid': 'Por favor, digite um endereço de e-mail válido'
        }
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}),
        error_messages={
            'required': 'A senha é obrigatória'
        },
        help_text="""
        <ul class="text-sm text-gray-600 dark:text-gray-400 pl-4 mt-1">
            <li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li>
            <li>Sua senha precisa conter pelo menos 8 caracteres.</li>
            <li>Sua senha não pode ser uma senha comum.</li>
            <li>Sua senha não pode ser inteiramente numérica.</li>
        </ul>
        """
    )
    password2 = forms.CharField(
        label='Confirme sua senha',
        widget=forms.PasswordInput(attrs={'placeholder': '••••••••'}),
        error_messages={
            'required': 'A confirmação de senha é obrigatória'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        error_messages = {
            'password_mismatch': 'As senhas não coincidem.'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove mensagens de ajuda padrão apenas para username e password2
        for fieldname in ['username', 'password2']:
            self.fields[fieldname].help_text = None
            
        self.helper = FormHelper()
        self.helper.form_tag = False  
        self.helper.disable_csrf = True