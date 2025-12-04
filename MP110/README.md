# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-16/

Changes done:
1. Added new `blogs/forms.py` with `BlogForm` to allow users to create a new blog.
2. Added new `new_blogs` url pattern in `blogs/urls.py`.
3. Added new view function for creating new blogs and added decorator to protect the page from anonymous users in `blogs/views.py`.
4. Created new `blogs/tempates/blogs/new_blog.html` for allowing users to login.
5. Added new `<a>` tag in nav bar left in `blogs/templates/blogs/base.html` for allowing logged in users to create a new blog.