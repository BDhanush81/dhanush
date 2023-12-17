from django.contrib import admin
from django.urls import path,include
from food import views

urlpatterns = [
    path('',views.fod),
    path('chicken',views.cen),
    path('egg',views.eg),
    path('fish',views.fis),
    
]
