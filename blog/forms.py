from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget
from taggit.forms import TagField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'slug',
            'category',
            'tags',
            'excerpt',
            'featured_image',
            'location',
            'content',
            'status',
        ]
        widgets = {
            'content': SummernoteWidget(),
        }
