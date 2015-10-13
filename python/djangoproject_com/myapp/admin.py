from django.contrib import admin

from myapp.models import PersonCustomManager, PersonCustomQuerySet

admin.site.register(PersonCustomManager)
admin.site.register(PersonCustomQuerySet)
