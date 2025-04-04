# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import CustomUserCreationForm 

def register_view(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro realizado com sucesso!")
            return redirect('flashcards:home_flashcards')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erro no campo {field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('flashcards:home_flashcards')
        else:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Senha incorreta para este usuário.")
            else:
                messages.error(request, "Usuário não encontrado.")
                
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


