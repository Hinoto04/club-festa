from django.contrib import admin
from .models import User, UserLoginLog

class HomeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'number']
    
admin.site.register(User, HomeAdmin)

class UserLoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'user_agent',)
    list_filter = ('ip_address', )
    date_hierarchy = 'created'

admin.site.register(UserLoginLog, UserLoginLogAdmin)