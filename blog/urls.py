from . import views
from django.urls import path


urlpatterns = [
    path('blog/', views.BlogPosts.as_view(), name='blog'),
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
