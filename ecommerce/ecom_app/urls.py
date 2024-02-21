from django.urls import path
from . import views

urlpatterns = [
    path ('' ,views.home, name = 'home'),
    path ('home' ,views.home, name = 'home'),
    path ('profile' ,views.profile, name = 'profile'),
    path('cart', views.cart, name = 'cart'),
    path('login', views.login, name = 'login'),
    path('create_account', views.create_account, name = 'create_account'),
    path('headphones', views.headphones, name = 'headphones'),
    path('mobile', views.mobile, name = 'mobile'),
    path('laptop', views.laptop, name = 'laptop'),
    path('t-shirt', views.t_shirt, name = 't-shirt'),
    path('AddLaptop', views.AddLaptop, name = 'AddLaptop'),
    path('AddT_shirt', views.AddT_shirt, name = 'AddT_shirt'),
    path('Head_phone', views.Head_phones, name = 'Head_phone'),
    path('Mobile_phones', views.Mobile_phone, name = 'Mobile_phones'),
]