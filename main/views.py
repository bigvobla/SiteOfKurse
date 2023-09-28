from django.shortcuts import render
from main import models


def login(request):
    return render(request, 'account/login.html')

def profle(request):
    return render(request, 'account/profile.html')

def index(request):
    name = request.POST.get("name")

    models.Product.objects.filter(name=name)

    return render(request, 'products/index.html')
