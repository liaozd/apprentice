from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True)
    num_pages = models.IntegerField(null=True)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.title


class Person(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    middle = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return "{}.{}.{}".format(self.first, self.middle, self.last)

    class Meta:
        ordering = ['last', 'first', 'middle']
        unique_together = ['first', 'last', 'middle']
        verbose_name_plural = 'people'



