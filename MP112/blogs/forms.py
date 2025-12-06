from .models import Blog, BlogPost
from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "description"]

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "body"]