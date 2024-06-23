from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login as signin_acc, logout, authenticate, get_user_model
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    category = Category.objects.all()
    return render (request, 'index.html',{'category':category})


def payment(request):
    return render (request, 'payment.html')

def cart(request):
    return render (request, 'cart.html')

# **************** Create account, Login and Logout Section ***********************

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

def product_list(request, name):
    
    prod = Products.objects.filter(category__name = name)
    
    for x in prod:
        x.final_price = x.Price - (x.Price * x.discount / 100)
    
    return render(request, 'mobile.html',{'prod':prod})

def Details(request, id):
    details = Products.objects.get(id = id)
    final_price = details.Price - (details.Price * details.discount / 100)
    return render(request, 'details.html',{'details':details,'final_price':final_price})

@login_required(login_url='login')
def user_profile(request, id):
    current_user_id = request.user.id
    
    if current_user_id != int(id):
        return render(request, 'access.html')
    
    user_profile = get_object_or_404(UserProfile, pro_id=id)
    user = user_profile.pro
    
    context = {
        'user_datas': user_profile,
        'user1': user
    }
    
    return render(request, 'profile.html', context)

# ---------- update user profile ------------------------

@login_required(login_url='login')
def update_profile(request, id):
    
    currentUser = request.user.id
    if currentUser != id:
        return render(request, 'access.html')
    
    update = UserProfile.objects.get(pro_id = id)
    
    if request.method =="POST":
        update.profile = request.FILES['profile']
        update.gender = request.POST['gender']
        update.mobile = request.POST['mobile']
        update.pro.username = request.POST['username']
        update.pro.first_name = request.POST['first_name']
        update.pro.last_name = request.POST['last_name']
        update.pro.email = request.POST['email']
        update.pro.save()
        update.save()
        
        messages.success(request, 'Profile Updated Successfully')
        return redirect(reverse('profile', kwargs={'id': id}))
    
    return render(request, 'update_profile.html',{'update':update})


def custom_page_not_found(request, exception):
    return render(request, 'error.html', status=404)