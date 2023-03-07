from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from blog import constants as CONST
from django.db.models import Count
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.template.loader import render_to_string
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

    # variables to show statistics on the main page
    total_posts = Post.objects.count()
    total_comments = Comment.objects.count()
    total_likes = Post.objects.aggregate(total_likes=Count('likes')).get('total_likes') or 0
    total_users = User.objects.count()

    return render(request, CONST.INDEX, {
        'trending': trending,
        'total_posts': total_posts,
        'total_comments': total_comments,
        'total_likes': total_likes,
        'total_users': total_users,
        })


def about(request):
    return render(request, CONST.ABOUT)


def contact(request):
    return render(request, CONST.CONTACT)

def rules(request):
    return render(request, CONST.RULES)


class FullPost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=2)  # 2 == published
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
        queryset = Post.objects.filter(status=2)  # 2 == published
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = post.likes.filter(id=self.request.user.id).exists()  # returns bool

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            messages.success(request, 'Thank you! Your comment is awaiting approval.')
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
            messages.success(request, 'Like removed!')
        else:
            post.likes.add(request.user)
            messages.success(request, 'Like added!')

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
            messages.success(request, 'Thank you! Your post was saved and you can check its status in the dashboard')
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
        messages.warning(request, 'Your post was deleted!')
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
            messages.success(request, 'Changes saved! You can check post status in your dashboard.')
            return redirect('user_account')
        else:
            return render(request, CONST.EDIT_POST, {'form': form})


@login_required
def dashboard_stats(request):
    author = request.user
    draft_count = Post.objects.filter(author=author, status=0).count()
    awaiting_moderation_count = Post.objects.filter(author=author, status=1).count()
    published_count = Post.objects.filter(author=author, status=2).count()

    context = {
        'published_count': published_count,
        'draft_count': draft_count,
        'awaiting_moderation_count': awaiting_moderation_count,
    }

    return context


@login_required
def user_account(request):
    user_posts = Post.objects.filter(author=request.user)
    dashboard_stats_data = dashboard_stats(request)
    return render(request, CONST.USER_ACCOUNT, {'user_posts': user_posts, 'dashboard_stats': dashboard_stats_data})


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
        # return posts with tags that are published, order descending
        return Post.objects.filter(tags=tag, status=2).order_by('-created_on')

    def get_context_data(self, **kwargs):
        context = super(TaggedPosts, self).get_context_data(**kwargs)
        context['tag'] = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
        return context
