from django.shortcuts import render

def log(request):
    return render(request,"login.html")

def checklogin(request):
    if request.method=='POST':
        un=request.POST['pname']
        ps=request.POST['password']

    if un=="dhanush" and ps=="dhanush313":
        return render(request,"next.html")
    else:
        dh="invalid"
        return render(request,"login.html",{"result":dh})

def nex(request):
    return render(request,"next.html")

def fog(request):
    return render(request,"forg.html")
# Create your views here.
