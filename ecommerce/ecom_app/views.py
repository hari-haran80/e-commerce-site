from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login as signin_acc, logout, authenticate, get_user_model
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


def home(request):
    category = Category.objects.all()
    return render (request, 'index.html',{'category':category})


def payment(request):
    return render (request, 'payment.html')

# ---------------------- Cart Section ------------------------

def cart(request):
    
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user = request.user)
        return render (request, 'cart.html', {'cart':cart})
    
    else:
        return redirect("login")
    

def AddToCart(request):
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty = data['product_qty']
            product_id = data['pid']
            product_status = Products.objects.get(id = product_id)
            
            if product_status:
                if Cart.objects.filter(user = request.user , product_id = product_id):
                    return JsonResponse({'status':"Product already added to cart"}, status = 200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user = request.user , product_id = product_id, quantity = product_qty)
                        return JsonResponse({'status':"Product added to cart"}, status = 200)
                    else:
                        return JsonResponse({'status':"No stack available"}, status = 200)
        else:
            return JsonResponse({'status':"Login to Continue"}, status = 200)
    else:
        return JsonResponse({'status':"invalid Access"}, status = 200)


def Delete_item (request, cid):
    cart_items = Cart.objects.get(id = cid)
    cart_items.delete()
    return redirect("cart")


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
    return render(request, 'mobile.html',{'prod':prod})

def Details(request, id):
    details = Products.objects.get(id = id)
    return render(request, 'details.html',{'details':details})

# -----------------  User Profile  ------------------------

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