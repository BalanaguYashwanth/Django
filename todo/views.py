from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth 
from .models import data
from django.contrib import messages

# Create your views here.
def base(request):
    if request.method=="POST":
        name=request.POST['name']
        user=data(name=name)
        user.save()
        des=data.objects.all()
        return render(request,'base.html',{'des':des});

    else:
        des=data.objects.all()
        return render(request,'base.html',{'des':des});

def delete(request,list_id):
    data1=data.objects.get(pk=list_id)
    data1.delete()
    return redirect('/');

