# Link to Blog - https://www.mostlypython.com/django-from-first-principles-part-2/

In this part a single python file with a simple html index page was built in django.

Steps:
1. Import django dependencies
2. setup setting by giving the `ROOT_URLCONF` as current file by giving `__name__`.
3. Create a view function called `index()` which returns a `HttpResponse` with a simple text.
4. Setup the url_patterns by giving in an empty string (which points to index) and associate it with the view function using `path`.
5. Assign `WSGIHandler()` to `application` to handle incoming requests.
6. Add `execute_from_command_line()` function to pass in commands to the script while running. (In this case `runserver`)
7. Start the server by running `python blogmaker_lite.py runserver`.
