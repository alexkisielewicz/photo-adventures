from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPosts.as_view(), name='blog'),
    path('blog/<slug:slug>/', views.FullPost.as_view(), name='full_post'),
]
