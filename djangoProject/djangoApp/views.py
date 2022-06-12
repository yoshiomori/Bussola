import importlib
import inspect

from django.db import models
from django.urls import reverse_lazy
from django.views import generic


def load_view_list():
    view_list = []
    module = importlib.import_module('djangoApp.models')
    for key in dir(module):
        item = getattr(module, key)
        if inspect.isclass(item) and issubclass(item, models.Model):
            class CreateView(generic.CreateView):
                model = item
                fields = '__all__'
            view_list.append(get_model_view(CreateView, item))

            class ListView(generic.ListView):
                model = item
            view_list.append(get_model_view(ListView, item))

            class DetailView(generic.DetailView):
                model = item
            view_list.append(get_model_view(DetailView, item))

            class UpdateView(generic.UpdateView):
                model = item
                fields = '__all__'
            view_list.append(get_model_view(UpdateView, item))

            class DeleteView(generic.DeleteView):
                model = item
                success_url = reverse_lazy(get_model_view_name(item, ListView))
            view_list.append(get_model_view(DeleteView, item))
    return view_list


def get_model_view(view_cls, model_cls):
    return type(get_model_view_name(model_cls, view_cls), (view_cls,), {})


def get_model_view_name(model_cls, view_cls):
    return model_cls.__name__ + view_cls.__name__
