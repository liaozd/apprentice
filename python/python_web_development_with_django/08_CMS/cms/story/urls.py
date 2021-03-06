from django.conf.urls import url, patterns
from story.models import Story

info_dict = {'queryset': Story.objects.all(), 'tempalte_object_name': 'story'}

urlpatterns = patterns('django.views.generic.list_detail',
                       url(r'^(?P<slug>[-\w]+)/$', 'object_detail', info_dict, name="cms-story"),
                       url(r'^$', 'object_list', info_dict, name="cms-home"),
                       )

urlpatterns += patterns('cms.views',
                        url(r'^category/(?P<slug>[-\w]+)/$', 'category', name="cms-category"),
                        url(r'^search/$', 'search', name="cms-search"),
                        )
