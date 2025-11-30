# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-12/

Changes done:
1. Moved blog models registration to `admin` site step to `blogs/admin.py`.
2. Moved `view` functions for blogs to `blogs/view.py`.
3. Moved `urlpatterns` for blogs to `blogs/urls.py`.
4. Made changes in the `urlpatterns` in `blogmaker_lite.py` to `include` the url patterns from `blogs/urls.py`
5. Set `app_name` in `blogs/urls.py` as `blogs`.
6. Moved blog templates to `blogs/templates/blogs` dir.
7. Changed path in `{% extends %}` in all templates.
8. Changed url in `{% url %}` in all anchor tags in html to `blogs/url`.