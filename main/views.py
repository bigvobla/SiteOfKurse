from django.shortcuts import render
from main import models


def login(request):
    return render(request, 'aut/login.html')

def profile(request):
    return render(request, 'users/userpage.html')

def signup(request):
    return render(request, 'aut/signup.html')

def index(request):
    name = request.POST.get("name")

    models.Product.objects.filter(name=name)

    return render(request, 'products/index.html')
