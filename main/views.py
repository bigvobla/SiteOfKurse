from django.shortcuts import render
from main import models


def login(request):
    return render(request, 'aut/login.html')

def profile(request):
    return render(request, 'users/buyer/buyerpage.html')

def signup(request):
    return render(request, 'aut/signup.html')
    
def main(request):
    return render(request, 'mainpage/mainpage.html')
    

def index(request):
    name = request.POST.get("name")

    models.Product.objects.filter(name=name)

    return render(request, 'products/index.html')
