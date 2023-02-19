from django.shortcuts import render
from django.views import generic
from .models import Post


class BlogPosts(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'blog.html'
    paginate_by = 8


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
