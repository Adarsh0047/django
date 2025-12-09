import os

from faker import Faker
faker = Faker()


import django
from django.core.management import call_command
import django.contrib.auth

# Load Settings
os.environ["DJANGO_SETTINGS_MODULE"] = "blogmaker_lite.settings"
django.setup()


# Flush Current Data
call_command("flush", "--noinput")
print(f"Flushed existing db.")

# Create SuperUser
os.environ["DJANGO_SUPERUSER_PASSWORD"] = "fake_pw"

cmd = "createsuperuser --username fake_admin"
cmd += " --email fake_email@example.com"
cmd += " --noinput"

cmd_parts = cmd.split()
call_command(*cmd_parts)


# Create a couple of users
for i in range(10):
    fake_user_name = faker.name()
    fake_pwd = faker.password(10)
    User = django.contrib.auth.get_user_model()
    user = User.objects.create(username=fake_user_name, password=fake_pwd)

from model_factories import BlogFactory, BlogPostFactory

# Generate Sample Blogs
for _ in range(10):
    BlogFactory.create()

# Generate Sample Blog Posts
for _ in range(100):
    BlogPostFactory.create()