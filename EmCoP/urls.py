from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('about/', views.about, name= 'About us'),
    path('logout/', views.logout, name='logout'),
    path('contact/', views.contact, name='contact us'),
    path('products/', views.products, name='Products'),
    path('join/', views.join, name='join us'),
    path('services/', views.services, name='services'),
]
