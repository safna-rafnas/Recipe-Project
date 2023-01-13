from django.shortcuts import render,redirect
from django.http import HttpResponse
from recipeadminApp.models import *
from . models import *
# Create your views here.
def userindex (request):
    data=Recipedb.objects.all()
    return render(request,'userindex.html',{'data':data})

def recipedetails(request):
    data=Recipedb.objects.all()
    return render(request,'recipedetails.html',{'data':data})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def singleblog(request):
    return render(request,'singleblog.html')

def details(request,id):
    data=Recipedb.objects.filter(id=id)
    return render(request,'details.html',{'data':data})

def adddata(request):
    if request.method=="POST":
        message=request.POST.get('message')
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        data=Contactdb(message=message,name=name,email=email,subject=subject)
        data.save()
    return redirect('userindex')

def register(request):
    return render(request,'register.html')

def rbdata(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        data=Registerdb(username=username,password=password,email=email,phone=phone)
        data.save()
    return redirect('userindex')

def loginuser(request):
    return render(request,'loginuser.html')

def login_data(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Registerdb.objects.filter(username=username, password=password).exists():
            data=Registerdb.objects.filter(username=username, password=password).values('email','phone','id').first()
            request.session['username']=username
            request.session['upassword']=password
            request.session['uemail']=data['email']
            request.session['uphone']=data['phone']
            request.session['uid']=data['id']
            return redirect('userindex')
        else:
            return render(request,'loginuser.html', {'msg':'Sorry Invalid user credentials'})
    else:
        return redirect('loginuser')
    
def userlogout(request):
    del request.session['username']
    del request.session['upassword']
    del request.session['uemail']
    del request.session['uphone']
    del request.session['uid']
    return redirect('userindex')