from django.urls import path
from . import views

urlpatterns = [

    path('' ,views.home, name = 'home'),
    path('home' ,views.home, name = 'home'),
    path('payment', views.payment, name = 'payment'),   

# ****************** Add to cart, Delete Items from Cart ***************
    
    path('cart', views.cart, name = 'cart'),
    path('AddToCart', views.AddToCart, name = 'AddToCart'),
    path('Delete_item/<int:cid>', views.Delete_item, name = 'Delete_item'),

# ****************** Login, Logout and Create User ***************

    path('login', views.login, name = 'login'),
    path('logout_user', views.logout_user, name = 'logout_user'),
    path('create_account', views.create_account, name = 'create_account'),
    path('resetPassword', views.Reset, name = 'resetPassword'),

# ****************** View Product Urls ***************************

    path('Products/<str:name>/', views.product_list, name = 'Products'),
    path('Details/<int:id>', views.Details, name = 'Details'),
    
# ****************** Profile Urls *****************************
    
    path('profile_update/<int:id>', views.update_profile, name='profile_update'),
    path('profile/<int:id>/' ,views.user_profile, name = 'profile'),
    
]