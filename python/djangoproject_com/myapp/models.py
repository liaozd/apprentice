from django.db import models
from django.utils.translation import ugettext_lazy as _


###################
# custom managers #
###################
class AuthorManager(models.Manager):
    def get_queryset(self):
        return super(AuthorManager, self).get_queryset().filter(role='A')


class EditorManager(models.Manager):
    def get_queryset(self):
        return super(EditorManager, self).get_queryset().filter(role='E')


class PersonCustomManager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=(('A', _('Author')),('E',_('Editor'))))

    people = models.Manager()
    # django interprets the first Manager defined in a class as the default manager,
    # other django approaches like 'dumpdata' will use that Manager exclusively for that model.
    authors = AuthorManager()
    editors = EditorManager()
    # you can call:
    # PersonCustomManager.authors.all()
    # PersonCustomManager.editors.all()
    # PersonCustomManager.people.all()


###################
# custom QuerySet #
###################
class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role='A')

    def editors(self):
        return self.filter(role='E')


# class PersonManager(models.Manager):
#     def get_queryset(self):
#         return PersonQuerySet(self.model, using=self._db)
#
#     def authors(self):
#         return self.get_queryset().authors()
#
#     def editors(self):
#         return self.get_queryset().editors()
# # In lieu of the above approach which requires duplicating methods on both
# # the QuerySet and the Manager, QuerySet.as_manager() can be used to create
# # an instance of Manager with a copy of a custom QuerySet’s methods.
# # The Manager instance created by QuerySet.as_manager() will be virtually
# # identical to the PersonManager from the previous example.

class PersonCustomQuerySet(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=(('A', _('Author')), ('E', _('Editor'))))
    # people = PersonManager()
    people = PersonQuerySet.as_manager()
    # you can call:
    # PersonCustomQuerySet.people.authors()
    # PersonCustomQuerySet.people.editors()
