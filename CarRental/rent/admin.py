from django.contrib import admin
from .models import RentCar
# Register your models here.
class rentAdmin(admin.ModelAdmin):
    model = RentCar
    search_fields = ('email', 'password', 'name','phone')
    list_display = [field.name for field in RentCar._meta.fields if field.name != "id"]

admin.site.register(RentCar, rentAdmin)