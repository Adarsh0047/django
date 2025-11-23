# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-8/

Changes done:
1. Added cards for each blog in `blogs.html`.
2. Added `STATIC_ROOT` dir in `settings.py`.
3. Ran the command `python manage.py collectstatic` to collect and store all static files (.js, .css) in the `STATIC_ROOT` dir. All the static files should be stored in one directory so that they can be served efficiently after deploying the app to a remote server.