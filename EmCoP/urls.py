from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('about/', views.about, name= 'About us'),
    path('logout/', views.user_logout, name='logout'),
    path('contact/', views.contact_view, name='contact us'),
    path('product_list/', views.product_list, name='Product_list'),
    path('join/', views.join, name='join us'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('products/', views.product_list, name='product_list'),
    path('emergency-alert/', views.emergency_alert, name='emergency_alert'),

    ]
