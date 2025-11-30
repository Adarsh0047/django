# Blog URL - https://www.mostlypython.com/django-from-first-principles-part-11/

Changes done:
1. Create a new script `generate_sample_data.py` which sets the settings, flushes the existing db, creates a new superuser, and creates random Blogs and BlogPosts.
2. Created a new script `model_factories.py` which uses `faker` and `factory` libraries which generates random titles and descriptions