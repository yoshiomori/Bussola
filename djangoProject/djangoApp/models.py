from django.db import models
from django.urls import reverse


class UrlModelMixin(object):
    def get_absolute_url(self):
        return reverse(f'{self.__class__.__name__}DetailView', kwargs=dict(pk=getattr(self, 'pk')))

    def get_delete_url(self):
        return reverse(f'{self.__class__.__name__}DeleteView', kwargs=dict(pk=getattr(self, 'pk')))

    def get_update_url(self):
        return reverse(f'{self.__class__.__name__}UpdateView', kwargs=dict(pk=getattr(self, 'pk')))

    def get_list_url(self):
        return reverse(f'{self.__class__.__name__}ListView')


class Counter(UrlModelMixin, models.Model):
    value = models.PositiveIntegerField()


class Project(UrlModelMixin, models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    revision = models.PositiveIntegerField()
    visibility = models.CharField(max_length=255)
    lastUpdateTime = models.DateTimeField()

    def __str__(self):
        return self.name
