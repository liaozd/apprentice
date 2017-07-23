from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from tutorial.quickstart import views
from snippets import views as snippets_views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
# router.register(r'snippet_detail', snippets_views.snippet_detail)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^snippets/', include('snippets.urls')),
]
