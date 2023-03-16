from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    # blog page with posts list url
    path('', views.BlogPosts.as_view(), name='blog'),

    # full post urls
    path('<slug:slug>/', views.FullPost.as_view(), name='full_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),

    # add, edit, delete urls
    path('add_post/', views.add_post, name='add_post'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('post/<slug:slug>/edit/', views.PostEdit.as_view(), name='edit_post'),

    # posts list by tag
    path('tag/<slug:tag_slug>/',
         views.TaggedPosts.as_view(), name='tagged_posts'),

    # allauth urls
    path('accounts/password_reset/',
         auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
