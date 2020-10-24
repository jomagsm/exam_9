from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:photo_detail')

# class ProductView(DetailView):
#     template_name = 'photo/photo_view.html'
#     model = Photo
#     paginate_reviews_by = 2
#     paginate_reviews_orphans = 0
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews, page, is_paginated = self.paginate_reviews(self.object)
#         if self.request.user.groups.filter(name='moderators').count():
#             context['reviews'] = reviews
#         else:
#             if self.request.user.is_authenticated:
#                 order_review = Review.objects.filter(product=self.object,author=self.request.user)
#             else:
#                 order_review = Review.objects.filter(product=self.object, status=True)
#             context['reviews'] = order_review
#         context['page_obj'] = page
#         context['is_paginated'] = is_paginated
#         return context
#
#     def paginate_reviews(self, product):
#         reviews = product.product_order.all()
#         if reviews.count() > 0:
#             paginator = Paginator(reviews, self.paginate_reviews_by, orphans=self.paginate_reviews_orphans)
#             page_number = self.request.GET.get('page', 1)
#             page = paginator.get_page(page_number)
#             is_paginated = paginator.num_pages > 1  # page.has_other_pages()
#             return page.object_list, page, is_paginated
#         else:
#             return reviews, None, False
