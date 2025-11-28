import factory
from faker import Faker
from random import randint

from blogs.models import Blog, BlogPost

faker = Faker()

def generate_title():
    return " ".join(faker.words()).title()

def generate_description():
    return faker.sentence(nb_words=20)

def generate_body():
    paragraphs = [
        faker.paragraph(randint(1, 5))
        for _ in range(randint(5, 20))
    ]
    return "\n\n".join(paragraphs)

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog
    
    title = factory.LazyFunction(generate_title)
    description = factory.LazyFunction(generate_description)

class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost
    
    title = factory.LazyFunction(generate_title)
    body = factory.LazyFunction(generate_body)
    blog = factory.Iterator(Blog.objects.all())