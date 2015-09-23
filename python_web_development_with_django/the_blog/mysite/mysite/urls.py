from django.conf.urls import include, url
from django.contrib import admin
from mysite.blog.views import archive

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', archive),
    url(r'^admin/', include(admin.site.urls)),
]
