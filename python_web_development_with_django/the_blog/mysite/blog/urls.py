from django.conf.urls import url
from blog.views import archive

urlpatterns = [
    url(r'^$', archive),
]
