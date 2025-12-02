# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-13/

Changes done:
1. Added new `accounts` app.
2. Added new `accounts/urls.py` app to handle user authentication.
3. Added new template `accounts/templates/registration/login.html` for login page.
4. Made changes in the `blogs/templates/blogs/base.html` nav bar to include the login, greeting and logout.
5. Added csrf middleware in `settings.py`, added `accounts` app in the `INSTALLED_APPS` var and also set the `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL` vars.