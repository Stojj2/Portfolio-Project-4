from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def scheduler(request):
    return render(request, 'scheduler.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')