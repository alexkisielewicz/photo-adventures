from . import views
from django.urls import path


urlpatterns = [
    path('', views.BlogPosts.as_view(), name='blog'),
]
