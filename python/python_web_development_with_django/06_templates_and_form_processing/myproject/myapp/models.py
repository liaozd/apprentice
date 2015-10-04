from django.db import models


class Person(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    middle = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['last', 'first', 'middle']
        unique_together = ['first', 'last', 'middle']
