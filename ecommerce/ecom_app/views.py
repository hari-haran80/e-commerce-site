from django.shortcuts import render,redirect
from .models import *
from .forms import *


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
    ear = Head_phone.objects.all()
    return render (request, 'headphone.html',{'ear': ear})

def mobile(request):
    mob = Mobile.objects.all()
    return render (request, 'mobile.html',{'mob':mob})

def laptop(request):
    product = Laptop.objects.all()
    return render (request, 'laptop.html',{'product':product})

def t_shirt(request):
    shirt = T_shirt.objects.all()
    return render (request, 't-shirt.html',{'shirt': shirt})


def AddLaptop(request):
    
    if request.method == 'POST':
        laptop = LaptopForm(request.POST, request.FILES)
    
        if laptop.is_valid():
            laptop.save()
    
        return redirect ('laptop')
    
    return render (request, 'add_product.html')



def AddT_shirt(request):
    
    if request.method == 'POST':
        t_shirt = t_shirtForm(request.POST, request.FILES)
    
        if t_shirt.is_valid():
            t_shirt.save()
    
        return redirect ('t-shirt')
    
    return render (request, 'addTshirt.html')


def Head_phones(request):
    
    if request.method == 'POST':
        headphone = HeadPhoneForm(request.POST, request.FILES)
    
        if headphone.is_valid():
            headphone.save()
    
        return redirect ('headphones')
    
    return render (request, 'addHeadPhone.html')


def Mobile_phone(request):
    
    if request.method == 'POST':
        Mob = MobileForm(request.POST, request.FILES)
    
        if Mob.is_valid():
            Mob.save()
    
        return redirect ('mobile')
    
    return render (request, 'addMobile.html')
    