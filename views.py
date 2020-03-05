from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from .models import data
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'todosign.html')


def base(request):
    if request.method=="POST":
        user = request.user
        name=request.POST['name']
        #user=data(name=name)
        #user.save()
        data.objects.create(name=name, user=user)
        des=data.objects.all()
        return render(request,'base.html',{'des':des});


    else:
        des=data.objects.all()
        return render(request,'base.html',{'des':des});

def delete(request,list_id):
    data1=data.objects.get(pk=list_id)
    data1.delete()
    return redirect('base');


def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('base')
        else:
            messages.info(request,'invalid')
            return redirect('login')

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        if password==password1:
            if User.objects.filter(username=username).exists():
                    messages.info(request,'username exists')
                    return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,email=email,username=username,password=password1,last_name=last_name)
                user.save()
                messages.info(request,'user saved')
                return redirect('login')
        else:
            messages.info(request,'invalid password')
            return render(request,'register.html')
    else:
        return render(request,'register.html')
    return redirect('/')









