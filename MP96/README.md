# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-6/

Changes done:
1. Created a new blogs page.
2. Created a new template for displaying all the blogs present in the context.
3. Added a new view function in `blogmaker_lite.py` which queries the db and gets all the blogs and passes it to the template in the render function.
4. Added names for the different urls in the url patterns so that they could be used easily.
5. Added anchor tag in `base.html` to navigate to index page.
6. Added anchor tag in `index.html` to go to blogs page.