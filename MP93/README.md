# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-4

Changes done:
1. Create `manage.py` which would be used for running the server / running other commands from cli.
2. Create an folder called `blogs` which is an app which contains the model for blog entity.
3. Added changes in `setting.py` to have `INSTALLED_APPS` and the database which needs to used for the `INSTALLED_APPS`.
4. Ran command `python manage.py makemigration blogs` to create a migration script for migrating the changes to db.
5. Ran command `python manage.py migrate` to migrate the changes to db.
6. Added changes in `settings.py` for enabling the admin site.
7. Added changes in `blogmaker_lite.py` for registering the blog app in the admin site and also added `urlpatterns` for the admin site. Here best practice would be to serve the admin site over a path other than `admin` for security purporses as automated attacks can be carried out over the `admin` site.
8. Created a new super user by running `python manage.py createsuperuser` to create a new sudo user to login to the admin site.