from django.shortcuts import render

def fod(request):
    return render(request,"foodie.html")

def cen(request):
    return render(request,"chicken.html")

def eg(request):
    return render(request,"egg.html")

def fis(request):
    return render(request,"fish.html")

# Create your views here.
