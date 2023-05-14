from django.shortcuts import render

def login(request):
    return render(request, 'myapp/login.html')

def dashboard(request):
    return render(request, 'myapp/dashboard.html')
