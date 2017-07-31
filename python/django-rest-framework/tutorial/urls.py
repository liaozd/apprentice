from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

from tutorial.quickstart import views
from snippets import views as snippet_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'snippets', snippet_views.SnippetViewSet)
router.register(r'snippet-users', snippet_views.UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
