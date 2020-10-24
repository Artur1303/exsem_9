from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'foto/index.html'
    model = Photo
    context_object_name = 'fotos'


class PhotoView(DetailView):
    template_name = 'foto/foto_view.html'
    context_object_name = 'fotos'
    model = Photo


class PhotoCreateView(PermissionRequiredMixin, CreateView):
    model = Photo
    template_name = 'foto/create_foto.html'
    form_class = PhotoForm
    permission_required = 'webapp.add_foto'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:foto_view', kwargs={'pk': self.object.pk})

class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'foto/update_foto.html'
    form_class = PhotoForm
    context_object_name = 'foto'
    permission_required = 'webapp.change_foto'

    def get_success_url(self):
        return reverse('webapp:foto_view', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)