from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers
from rest_framework.schemas import get_schema_view

from snippets import views as snippet_views
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippets', snippet_views.SnippetViewSet)
router.register(r'snippet-users', snippet_views.UserViewSet)

schema_view = get_schema_view(title='Pastebin API')


urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
