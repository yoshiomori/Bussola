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
