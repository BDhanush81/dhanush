from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from todo.models import adm

def admin(request):
    return render(request,"admin.html")

def storedata(request):
    if request.method=="POST":
        to=request.POST['todo']
        do=request.POST['key']
        dr=request.POST['reg']

        std=adm()
        std.reg=dr
        std.todo=to
        std.status=do

        std.save()
        de="saved"
        return render(request,"admin.html",{"result":de})

def table(request):
    du=adm.objects.all()
    return render(request,"table.html",{"net":du})

def update(request,d):
    du=adm.objects.get(id=d)
    return render(request,"update.html",{"dha":du})

def changetodo(request):
    if request.method=="POST":
        to=request.POST['todo']
        do=request.POST['key']
        dr=request.POST['reg']

        std=adm.objects.get(reg=dr)
        std.status=do
        std.todo=to
        
        std.save()
        return HttpResponseRedirect('table')

def delete(request,d):
    du=adm.objects.get(id=d)
    du.delete()
    return HttpResponseRedirect('/table')

def productserach(request):
    se=request.GET.get('search')
    result=adm.objects.filter(status=se)
    if result:
        results=result
    elif (result!=se):
        return HttpResponseRedirect('/table')
    else:
        results=False
    return render(request,"table.html",{"net":results})


# Create your views here.
