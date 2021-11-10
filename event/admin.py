from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    search_fields = ['title']
    
admin.site.register(Event, EventAdmin)