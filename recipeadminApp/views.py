from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from recipeuserApp.models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def adminindex(request):
    recipecount = Recipedb.objects.all().count()
    messagecount = Contactdb.objects.all().count()
    usercount = Registerdb.objects.all().count()
    return render(request,'adminindex.html',{'recipecount':recipecount,'messagecount':messagecount,'usercount':usercount})

def addrecipe(request):
    return render(request,'addrecipe.html')

def viewrecipe(request):
    data=Recipedb.objects.all()
    return render(request,'viewrecipe.html',{'data':data})

def recipe(request):
    if request.method=="POST":
        recipename=request.POST.get('recipename')
        image=request.FILES['image']
        instraction=request.POST.get('instraction')
        ingredients=request.POST.get('ingredients')
        data=Recipedb(recipename=recipename,image=image,instraction=instraction,ingredients=ingredients)
        data.save()
    return redirect('viewrecipe')

def edit(request,id):
    data=Recipedb.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})

def update(request,id):
    if request.method=="POST":
        recipename=request.POST.get('recipename')
        instraction=request.POST.get('instraction')
        ingredients=request.POST.get('ingredients')
        try:
          image=request.FILES['image']
          fs=FileSystemStorage()
          file=fs.save(image.name,image)
        except MultiValueDictKeyError:
          file=Recipedb.objects.get(id=id).image
        Recipedb.objects.filter(id=id).update(recipename=recipename,image=file,instraction=instraction,ingredients=ingredients)
    return redirect('viewrecipe')
def delete(request,id):
    Recipedb.objects.filter(id=id).delete()
    return redirect('viewrecipe')
    
def message(request):
    data=Contactdb.objects.all()
    return render(request,'message.html',{'data':data})

def adminlogin(request):
    return render(request,'adminlogin.html')

def rtable(request):
    db=Registerdb.objects.all()
    return render(request,'rtable.html',{'data':db})

def adlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None :
            login(request,user)
            request.session['upusername']=username
            request.session['uppassword']=password
            return redirect('adminindex')   
        else:
            return render(request,'adminlogin.html', {'msg':'Sorry Invalid user credentials'})
    else:
        return render(request,'adminindex.html')

def adminlogout(request):
    del request.session['upusername']
    del request.session['uppassword']
    return redirect('adminlogin')
