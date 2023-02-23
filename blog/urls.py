from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPosts.as_view(), name='blog'),
    path('<slug:slug>/', views.FullPost.as_view(), name='full_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/', views.add_post, name='add_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]
