#post/admin.py
from django.contrib import admin

from .models import (
    BlogPost,
    Category,
    Comment,
)


class CommentInline(admin.StackedInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]


admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Comment)
