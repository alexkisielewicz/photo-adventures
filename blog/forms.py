from .models import Comment, Post
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=((0, 'Save as draft (finish later)'), (1, 'Publish (will be awaiting moderation)')), widget=forms.RadioSelect())

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
            'title': forms.TextInput(attrs={'id': 'idTitle', 'placeholder': 'Post title'}),
            'slug': forms.TextInput(attrs={'slug': 'idSlug', 'placeholder': 'Avoid using special characters or spaces (e.g. my-great-blog-post)'}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please write a teaser that entices readers to read the full post.'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Dublin, Ireland'}),
            'content': SummernoteWidget(),
        }
