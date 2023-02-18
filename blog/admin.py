from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# customize post display in admin panel
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('status', 'author', 'category', 'created_on')
    list_display = ('title', 'slug', 'author', 'category', 'featured', 'status', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')


# customize comments display in admin panel
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'name')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
