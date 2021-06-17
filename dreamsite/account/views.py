from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from account.forms import RegisterForm
from .models import Account
from django.views.generic import CreateView

from . import forms

def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'account/signup.html', {'form': form})
