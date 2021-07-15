from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from index.models import Car
from datetime import datetime, date

# Create your models here.
class RentCar(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    time = models.CharField(max_length=100)
    cost = models.CharField(max_length=10)

    def startdatetime(self):
        print(self)
        return datetime.strptime(str(self.start), '%Y-%m-%dT%H:%M').strftime('%d-%m-%Y %H:%M')
    
    def enddatetime(self):
        return datetime.strptime(str(self.end), '%Y-%m-%dT%H:%M').strftime('%d-%m-%Y %H:%M')