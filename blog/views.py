from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Post
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from taggit.models import Tag


class BlogPosts(generic.ListView,):
    """
    Class view for all blog posts. Returns all posts to blog.html template.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 5


class PostList(generic.ListView):

    model = Post
    context_object_name = 'post'
    template_name = 'index.html'


def index(request):
    trending = Post.objects.filter(status=1).annotate(
        like_count=Count('likes')).order_by('-like_count')[:3]
    return render(request, 'index.html', {'trending': trending})

# Add - top commented
# Add - last 3


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# Should this be a class view with pagination?
@login_required
def user_account(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, 'user_account.html', {'user_posts': user_posts})


class FullPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'full_post.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'full_post.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('full_post', args=[slug]))


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == "POST":
        post.delete()
        return redirect('user_account')
    else:
        return render(request, 'delete_post.html', {'post': post})


class PostEdit(View):

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(instance=post)
        return render(request, 'edit_post.html', {'form': form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = form.cleaned_data['status']
            content = post.content
            if post.status == 1:  # "Publish now"
                post.save()
                return redirect('full_post', slug=post.slug)
            else:  # "Save as draft"
                post.save()
                return redirect('user_account')
        else:
            return render(request, 'edit_post.html', {'form': form})


# def dashboard_stats(request):
#     author = request.user
#     published_count = Post.objects.filter(author=author, status=1).count()
#     draft_count = Post.objects.filter(author=author, status=0).count()

#     context = {
#         'published_count': published_count,
#         'draft_count': draft_count,
#     }

#     return render(request, 'user_account.html', context)


class TaggedPosts(generic.ListView):
    model = Post
    template_name = 'blog.html'
    paginate_by = 5

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags=tag).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(TaggedPosts, self).get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return context
