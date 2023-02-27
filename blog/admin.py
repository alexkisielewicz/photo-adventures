from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Customize post display in admin panel
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('status', 'author', 'category', 'created_on')
    list_display = ('title', 'slug', 'author', 'category', 'get_tags',
                    'featured', 'status', 'created_on')
    search_fields = ('title', 'content')
    summernote_fields = ('content')

    # Method to add tags to admin panel view as described in Taggit docs
    def get_tags(self, obj):
        return ', '.join(o for o in obj.tags.names())

    # actions in admin panel to change status of selected post/s
    @admin.action(description='Mark selected posts as Draft')
    def mark_as_draft(modeladmin, request, queryset):
        queryset.update(status=0)

    @admin.action(description='Mark selected posts as Sent for moderation')
    def mark_as_sent_for_moderation(modeladmin, request, queryset):
        queryset.update(status=1)

    @admin.action(description='Mark selected posts as Published')
    def mark_as_published(modeladmin, request, queryset):
        queryset.update(status=2)

    actions = [mark_as_published, mark_as_draft, mark_as_sent_for_moderation]


# Customize comments display in admin panel
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'name')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
