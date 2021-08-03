from django.contrib import admin
from .models import User

class HomeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'number']
    
admin.site.register(User, HomeAdmin)