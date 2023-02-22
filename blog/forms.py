from .models import Comment, Post
from django import forms


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
            'excerpt',
            'featured_image',
            'location',
            'content',
            ]

