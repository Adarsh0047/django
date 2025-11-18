from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line

settings.configure(
    ROOT_URLCONF = __name__,
    DEBUG=True,
    SECRET_KEY="secret-key"
)

def index(request):
    return HttpResponse("Welcome to BlogMakerLite...")

urlpatterns = [
    (path("", index))
]
application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()