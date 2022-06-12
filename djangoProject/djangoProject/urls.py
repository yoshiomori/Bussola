"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views import generic

from djangoApp.views import load_view_list


def get_url(view_class):
    if issubclass(view_class, (generic.DetailView, generic.UpdateView, generic.DeleteView)):
        tail = '/<int:pk>/'
    else:
        tail = '/'
    return view_class.__name__ + tail


urlpatterns = [
    path('admin/', admin.site.urls),
] + [path(get_url(view_class), view_class.as_view(), name=view_class.__name__) for view_class in load_view_list()]
