from django.http import request
from .models import RentCar
from django.shortcuts import redirect, render
from index.models import Car
from django.views.generic.list import ListView
from accounts.models import User


# Create your views here.
def successful(request,pk):
    user = request.user
    car = Car.objects.get(id=pk)
    start =  request.POST['startTime']
    end =  request.POST['endTime']
    time =  request.POST['hours']
    cost =  request.POST['cost']
    rentcar = RentCar.objects.create(user=user, car=car, start=start, end=end, time=time, cost=cost)
    rentcar.save()
    return render(request, "rentSuccessful.html", {'rentcar':rentcar})

def rentcar(request, pk):
    car=Car.objects.get(id=pk)
    return render(request, 'rent.html', {'car':car})

class historylist(ListView):
    model=RentCar
    template_name='history.html'
    
    def get_queryset(self):
        return RentCar.objects.filter(user=self.request.user)
