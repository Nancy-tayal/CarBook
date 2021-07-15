from django.contrib import admin
from .models import Car
# Register your models here.
class carAdmin(admin.ModelAdmin):
    model = Car
    search_fields = ('email', 'password', 'name','phone')
    list_display = [field.name for field in Car._meta.fields if field.name != "id"]

admin.site.register(Car,carAdmin)