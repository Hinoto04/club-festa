from django.contrib import admin
from .models import Club

class ClubAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
admin.site.register(Club, ClubAdmin)