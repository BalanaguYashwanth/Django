from django import forms
from django.forms import ModelForm
from .models import data

class EventForm(ModelForm):
    name=forms.CharField(max_length=100)
    class Meta:
        model = data
        fields = ('user','name')

# views.py
from django.contrib.auth.decorators import login_required

@login_required
def create_event(request):
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()
        return render(..., {'form': form})