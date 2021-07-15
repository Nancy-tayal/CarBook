from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    search_fields = ('email', 'password', 'name','phone')
    list_display = [field.name for field in User._meta.fields if field.name != "id"]
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name','phone')}
         ), ('Permissions', {'fields': ('is_staff', 'is_active')}),)
    
admin.site.register(User,UserAdmin)