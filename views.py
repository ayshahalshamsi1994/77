
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'aiacademy_app/index.html')

def user_login(request):
    if request.method == "POST":
        email = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'aiacademy_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'aiacademy_app/login.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'aiacademy_app/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'aiacademy_app/dashboard.html', {'user': request.user})
