from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path("", views.index, name="index"),
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/<int:blog_id>", views.blog, name="blog"),
    path("posts/<int:post_id>", views.post, name="post"),
    path("new_blogs/", views.new_blog, name="new_blog"),
    path("new_posts/<int:blog_id>", views.new_blog_post, name="new_blog_post")
    ]