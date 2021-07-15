from django.db import models

# Create your models here.

class Car(models.Model):
    
    name = models.CharField(unique=True,max_length=100)
    engine = models.CharField(max_length=50)
    door = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    seats = models.IntegerField()
    mileage = models.CharField(max_length=20)
    luggage = models.IntegerField()
    fuel = models.CharField(max_length=20)
    transmission=models.CharField(max_length=30)
    instock = models.IntegerField()
    rent = models.IntegerField()
    offer = models.BooleanField(default=False)