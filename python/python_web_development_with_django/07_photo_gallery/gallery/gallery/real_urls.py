from django.contrib import admin
from django.conf.urls import include, url, patterns

urlpatterns = patterns('',
        url(r'^admin/(.*)', admin.site.urls),
        url(r'^', include('item.urls')),
        )

