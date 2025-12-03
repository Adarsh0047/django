# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-15/

Changes done:
1. Added new `owner` foreign field for the blog model in `blogs/models.py`.
2. Made changes in the `generate_sample_data.py` to create random users.
3. Made changes in `model_factories.py` to select random user for each blog.
4. Made change in `blogs/templates/blogs/blog.html` to display the `blog.owner.username`.
5. Made change in `blogs/templates/blogs/blogs.html` to display the `blog.owner.username`.
6. Made change in `blog/templates/blogs/post.html` to display the `blog.owner.username`.