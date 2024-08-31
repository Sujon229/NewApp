from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('productList', views.show_product, name='productList'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
