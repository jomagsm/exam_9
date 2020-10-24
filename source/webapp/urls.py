from django.urls import path

from webapp.views import IndexView, PhotoDetailView, PhotoCreateView, PhotoUpdateView, ProductDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_view'),
    path('photo_create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo_update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo_delete/<int:pk>/', ProductDeleteView.as_view(), name='photo_delete')
]