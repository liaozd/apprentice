from io import BytesIO
import os
import sys
from PIL import Image

from django import forms
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseBadRequest

# This is created by project template

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', '(j=!b1$2&4fpz*4#pz1=m2r37ue2$v=gbtn*@3ig6a8n1%z2^b')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')


settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)


class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""

    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)

    def generate(self, image_format='PNG'):
        """Generate an image of the given type and return as raw bytes."""
        height = self.cleaned_date['height']
        width = self.cleaned_data['width']
        image = Image.new('RGB', (width, height))
        content = BytesIO()
        image.save(content, image_format)


def placeholder(request, width, height):
    form = ImageForm({'height':height, 'width': width})
    if form.is_valid():
        height = form.cleaned_data['height']
        width = form.cleaned_data['width']
        return HttpResponse('Ok')
    else:
        return HttpResponseBadRequest('Invalid Image Request')


def index(request):
    return HttpResponse('Hello World')


urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder,
        name='placeholder'),
    url(r'^$', index, name='homepage'),
)


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

    # django-admin.py startproject placeholder --template=chap1/project_name
    # to start a new project by this template

    # hostname $ export DEBUG=off
    # hostname $ export ALLOWED_HOSTS=localhost,example.com
    # hostname $ python hello.py runserver