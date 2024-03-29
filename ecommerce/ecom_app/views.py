from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login as signin_acc, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render (request, 'index.html')

def profile(request):
    return render (request, 'profile.html')

def cart(request):
    return render (request, 'cart.html')

# **************** Create Login and Logout Section ***********************

def login(request):
    if request.method == "POST":
        username = request.POST ['username']
        password = request.POST ['password']
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            signin_acc(request, user)
            return redirect('home')
        
        else:
            messages.error(request, 'enter correct username and password')
        
    return render (request, 'login_amazon.html')

def create_account(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            data = User.objects.create_user(
                username = username,
                email = email,
                password = password1,
            )
            
            data.is_staff = True
            data.save()
            data.set_password(password1)
            
            return redirect('login')
            
        else:
            messages.error(request, 'Password MisMatched')
            return render (request, 'create.html')
            
            
    return render (request, 'create.html')


def logout_user(request):
    logout(request)
    
    return redirect('login' )


def Reset(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = get_user_model().objects.get(username = username)
        
        except:
            messages.error(request, 'User Not Found!') 
            return render (request, 'reset.html')
            
        user.set_password(password)
        user.save()
        
        messages.success(request, f"{username}'s Password has been reset")
        return redirect('login')
    
    return render(request, 'reset.html')

# ********************* View Product Section **********************

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

# ****************** Add Products section *******************

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
    