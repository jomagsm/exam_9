from django.urls import path, include
from rest_framework import routers

from api.views import AddFavoriteView, RemoveFavoritesView

app_name = 'api'

urlpatterns = [
    path('add_favorites/<int:pk>/', AddFavoriteView.as_view(), name='add_favorites'),
    path('remove_favorites/<int:pk>/', RemoveFavoritesView.as_view(), name='remove_favorites'),

]
