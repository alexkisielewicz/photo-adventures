from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Tuple for post status
STATUS = (
    (0, 'Draft'), (1, 'Published')
)


class Post(models.Model):
    POST_CATEGORIES = (
        ('adventure', 'Adventure'),
        ('travel', 'Travel'),
        ('nature', 'Nature'),
        ('landscape', 'Landscape'),
        ('aerial', 'Aerial'),
        ('wildlife', 'Wildlife'),
        ('street', 'Street'),
        ('architecture', 'Architecture'),
    )

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photo_adventures')
    category = models.CharField(choices=POST_CATEGORIES, max_length=20, default='adventure')
    excerpt = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    location = models.CharField(max_length=100, unique=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    featured = models.BooleanField(default=False, verbose_name='featured post')

    # Descending order of Posts
    class Meta:
        ordering = ['-created_on']

    # Method to return string object
    def __str__(self):
        return self.title

    # Method to return total number of likes
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # Ascending order of Comments
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
