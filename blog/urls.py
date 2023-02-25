from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPosts.as_view(), name='blog'),
    path('<slug:slug>/', views.FullPost.as_view(), name='full_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.add_post, name='add_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('post/<slug:slug>/edit/', views.PostEdit.as_view(), name='edit_post'),
    path('tag/<slug:tag_slug>/', views.TaggedPosts.as_view(), name='tagged_posts'),
]
