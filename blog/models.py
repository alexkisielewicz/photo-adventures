from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from blog import constants as CONST
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase


class Post(models.Model):
    """
    Model of the blog post
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='photo_adventures')
    category = models.CharField(choices=CONST.POST_CATEGORIES, max_length=20,
                                default='adventure')
    excerpt = models.TextField(blank=False)
    featured_image = CloudinaryField('image', default='placeholder')
    location = models.CharField(max_length=100, unique=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=CONST.STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    featured = models.BooleanField(default=False, verbose_name='featured post')
    tags = TaggableManager()

    class Meta:
        """
        Class to set descending order of Posts in Admin Panel
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Method to return string object
        """
        return self.title

    def number_of_likes(self):
        """
        Method to rerunt total number of likes
        """
        return self.likes.count()

    def number_of_comments(self):
        """
        Method to return total number of approved comments
        """
        return self.comments.filter(approved=True).count()


class TaggedPost(TaggedItemBase):
    """
    Class represents model of post with tags created
    by TaggableManager (taggit)
    """
    content_object = models.ForeignKey('Post', on_delete=models.CASCADE)


class Comment(models.Model):
    """
    Class represents comments that can be added to posts
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Class to set ascending order of Comments
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Method to return string
        """
        return f'Comment {self.body} by {self.name}'
