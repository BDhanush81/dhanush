from django.contrib import admin
from django.urls import path,include
from pint import views

urlpatterns = [
    path('',views.log),
    path('checklogin',views.checklogin),
    path('next',views.nex),
    path('forg',views.fog),
]