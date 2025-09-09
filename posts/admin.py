from django.contrib import admin
from .models import Post, Like, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "content", "total_likes", "created_at")

admin.site.register(Post, PostAdmin)
admin.site.register(Like)
admin.site.register(Comment)
