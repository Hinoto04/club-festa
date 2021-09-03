from django.contrib import admin
from .models import Notice, Post, Comment

class PostAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Notice, PostAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, PostAdmin)