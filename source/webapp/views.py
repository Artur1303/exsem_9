from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from webapp.models import Photo


class IndexView(ListView):
    template_name = 'foto/index.html'
    model = Photo
    context_object_name = 'fotos'


class PhotoView(DetailView):
    template_name = 'foto/foto_view.html'
    context_object_name = 'fotos'
    model = Photo