# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-17/

Changes done:
1. Added `BlogPostForm` in `blogs/forms.py` for creating a form for blog posts.
2. Added `new_posts/<int:blog_id>` urlpattern in `blogs/urls.py`.
3. Added `new_blog_post()` view function in `blogs/views.py` for creating new blogpost.
4. Added `blogs/templates/blogs/new_post.html` template for new post.
5. Modified `blogs/templates/blogs/blog.html` to display new blog post button.