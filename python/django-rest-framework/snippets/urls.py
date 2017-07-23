from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^$', views.snippet_list),
    url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),
]