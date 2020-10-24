from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CreateView, DeleteView

app_name = 'api'


urlpatterns = [
    path('favorites/<int:pk>/delete/', DeleteView.as_view(), name='favorites_delete'),
    path('favorites/add/<int:pk>/', CreateView.as_view(), name='favorites_create')


]