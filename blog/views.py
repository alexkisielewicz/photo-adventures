from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.db.models import Count
from .models import Post
from .forms import CommentForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from blog import constants as CONST
from taggit.models import Tag


class BlogPosts(generic.ListView,):
    """
    Class view for all blog posts. Returns all posts to blog.html template.
    """
    model = Post
    queryset = Post.objects.filter(status=2).order_by('-created_on')  # 2 = published
    template_name = CONST.BLOG
    paginate_by = CONST.PAGINATION


class PostList(generic.ListView):
    model = Post
    context_object_name = 'post'
    template_name = CONST.BLOG


def index(request):
    # filter only published posts with more than 0 likes
    trending = Post.objects.filter(status=2, likes__gt=0).annotate(
        like_count=Count('likes')).order_by('-like_count')[:3]
    return render(request, CONST.INDEX, {'trending': trending})


def about(request):
    return render(request, CONST.ABOUT)


def contact(request):
    return render(request, CONST.CONTACT)


# Should this be a class view with pagination?
@login_required
def user_account(request):
    user_posts = Post.objects.filter(author=request.user)
    return render(request, CONST.USER_ACCOUNT, {'user_posts': user_posts})


class FullPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=2)  # 2 = published
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = post.likes.filter(id=self.request.user.id).exists()

        return render(
            request,
            CONST.FULL_POST,
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
        liked = post.likes.filter(id=self.request.user.id).exists()  # returns bool

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
            CONST.FULL_POST,
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            },
        )


class PostLike(LoginRequiredMixin, View):
    """
    Class based view that allows users to like posts.
    It toggles to add/remove post.likes
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('full_post', args=[slug]))


@login_required
def add_post(request):
    """
    Function based view that allows users to add new posts.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('user_account')
    else:
        form = PostForm()
    return render(request, CONST.ADD_POST, {'form': form})


@login_required
def delete_post(request, slug):
    """
    Function based view that allows users to delete their posts.
    """
    post = get_object_or_404(Post, slug=slug, author=request.user)
    if request.method == "POST":
        post.delete()
        return redirect('user_account')
    else:
        return render(request, CONST.DELETE_POST, {'post': post})


class PostEdit(View):
    """
    Class based view to allow users to edit posts.
    It uses post model and post form to read and update values.
    """
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(instance=post)
        return render(request, CONST.EDIT_POST, {'form': form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            content = post.content
            post.save()
            form.save_m2m()
            return redirect('user_account')
        else:
            return render(request, CONST.EDIT_POST, {'form': form})

@login_required
def dashboard_stats(request):
    author = request.user
    draft_count = Post.objects.filter(author=author, status=0).count()
    awaiting_moderation_count = Post.objects.filter(author=author, status=1).count()
    published_count = Post.objects.filter(author=author, status=2).count()

    print(published_count)
    print(draft_count)
    print(awaiting_moderation_count)

    context = {
        'published_count': published_count,
        'draft_count': draft_count,
    }

    return render(request, CONST.USER_ACCOUNT, context)


class TaggedPosts(generic.ListView):
    """
    It renders a list of all posts with specific slug.
    Posts are displayed 5 per page using blog.html template.
    """
    model = Post
    template_name = CONST.BLOG
    paginate_by = CONST.PAGINATION

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags=tag).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(TaggedPosts, self).get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return context
