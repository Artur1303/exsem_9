from django.urls import path
from webapp.views import IndexView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('foto/<int:pk>/', PhotoView.as_view(), name='foto_view'),
    path('foto/add/', PhotoCreateView.as_view(), name='foto_create'),
    path('foto/<int:pk>/update/', PhotoUpdateView.as_view(), name='foto_update'),
    path('product/<int:pk>/delete/', PhotoDeleteView.as_view(), name='foto_delete'),

]