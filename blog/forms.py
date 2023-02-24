from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        

class PostForm(forms.ModelForm):
    STATUS_CHOICES = (
        (0, 'Save as draft'),
        (1, 'Publish now'),
    )
    status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Post
        fields = [
        'title',
        'category',
        'excerpt',
        'featured_image',
        'location',
        'content',
        'status',
    ]
        widgets = {
            'content': SummernoteWidget(),
        }