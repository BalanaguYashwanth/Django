from django.shortcuts import render,redirect
from .models import details

# Create your views here.
def home(request):
    return render(request,'homex.html')


def data(request):
    if request.method=="POST":
        person=request.POST['person']
        zone=request.POST['zone']
        place=request.POST['place']
        details.objects.create(zone=zone,place=place,person=person)
        all=details.objects.all()
        return redirect(home)
    else:
        all=details.objects.all()
        return render(request,'homey.html',{'all':all})


