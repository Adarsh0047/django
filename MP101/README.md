# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-9/

Changes done:
1. Added new `urlpatterns` for `blog_posts` which is a dynamic `blog` url with the blog id.
2. Created a `blog` view func to query all `blog_posts` related to a `blog_id`.
3. Created `blog.html` inside `templates` folder to display each blog post along with its date created and body.
4. Modified the `header` div tag for the `card` div in `blogs.html` to have an anchor to the blog_posts with the id.
5. Added some query cmds in `shell.cmds.py`.