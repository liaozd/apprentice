from django.contrib import admin
from books.models import *


class BookInline(admin.StackedInline):
    model = Book


class AuthorInline(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Book)
admin.site.register(Author, AuthorInline)
