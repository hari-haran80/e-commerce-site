from django.shortcuts import render,redirect


def home(request):
    return render (request, 'index.html')

def profile(request):
    return render (request, 'profile.html')

def cart(request):
    return render (request, 'cart.html')

def login(request):
    return render (request, 'login_amazon.html')

def create_account(request):
    return render (request, 'create.html')

def headphones(request):
    return render (request, 'headphone.html')

def mobile(request):
    return render (request, 'mobile.html')

def laptop(request):
    return render (request, 'laptop.html')

def t_shirt(request):
    return render (request, 't-shirt.html')