from django.shortcuts import render
from .models import Car
# Create your views here.

def home(request):
    cars= Car.objects.all()
    return render(request, 'home.html', {'cars' : cars})
    
def displaycars(request):
    cars= Car.objects.all()
    return render(request, 'displaycars.html', {'cars' : cars})