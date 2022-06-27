from django.urls import path

from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/blog-1', views.post_detail, name="post-details")
]
