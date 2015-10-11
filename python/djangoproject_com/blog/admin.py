from django.contrib import admin

from blog.models import Entry, Blog, Author


admin.site.register(Entry)
admin.site.register(Blog)
admin.site.register(Author)
