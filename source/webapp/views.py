from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from webapp.forms import PhotoForm, PhotoCreateForm
from webapp.models import Photo


class IndexView(ListView):
    template_name = 'photo/index.html'
    model = Photo
    context_object_name = 'photos'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        data = Photo.objects.all()
        data.order_by('-created_at')
        return data


class PhotoDetailView(DetailView):
    template_name = 'photo/photo_view.html'
    context_object_name = 'photo'
    model = Photo
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        return reverse('webapp:photo_detail')


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    form_class = PhotoCreateForm
    template_name = 'photo/photo_create.html'
    permission_required = 'webapp.add_photo'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/product_update.html'
    permission_required = 'webapp.change_product'

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.author or self.request.user.is_superuser \
               or self.request.user.has_perm('webapp.change_photo')

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = reverse_lazy('webapp:index')
    permission_required = 'webapp.delete_photo'

    def test_func(self):
        photo = self.get_object()
        return self.request.user == photo.author or self.request.user.is_superuser \
               or self.request.user.has_perm('webapp.delete_photo')