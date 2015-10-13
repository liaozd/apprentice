from django.db import models
from django.utils.translation import ugettext_lazy as _

##############################################
# using multiple managers on the same model. #
##############################################
class AuthorManager(models.Manager):
    def get_queryset(self):
        return super(AuthorManager, self).get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super(EditorManager, self).get_queryset().filter(role='E')


class Person_custom_manager(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=(('A', _('Author')),('E',_('Editor'))))

    people = models.Manager()
    # django interprets the first Manager defined in a class as the default manager,
    # other django approaches like 'dumpdate' will use that Manager exclusively for that model.
    authors = AuthorManager()
    editors = EditorManager()
    # you can call:
    # Person_custom_manager.authors.all()
    # Person_custom_manager.editors.all()
    # Person_custom_manager.people.all()


##############################################
# using multiple managers on the same model. #
##############################################
class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role='A')

    def editors(self):
        return self.filter(role='E')


