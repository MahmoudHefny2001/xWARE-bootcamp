from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as AUTH_LOGIN
from django.shortcuts import render, redirect
from .forms import SignupForm
# Create your views here.

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            AUTH_LOGIN(request, user)
            return redirect('home')
    return render(request, 'signup.html', {'form': form})
