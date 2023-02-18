from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Tuple for post status
STATUS = (
    (0, "Draft"), (1, "Published")
)


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)

    # Method to return string object
    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photo_adventures")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    excerpt = models.TextField(blank=True)
    featured_image = CloudinaryField("image", default='placeholder')
    location = models.CharField(max_length=100, unique=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    featured = models.BooleanField(default=0)

    # Descending order of Posts
    class Meta:
        ordering = ["-created_on"]

    # Method to return string object
    def __str__(self):
        return self.title

    # Method to return total number of likes
    def number_of_likes(self):
        return self.likes_count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    # Ascending order of Comments
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
