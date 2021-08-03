
from django.shortcuts import render

def index(request):
    return render(request, 'home/home_main.html')

def register(request):
    return render(request, 'home/home_register.html')

def login(request):
    return render(request, 'home/home_login.html')