from django.urls import path
from webapp.views import IndexView, PhotoView, PhotoCreateView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('foto/<int:pk>/', PhotoView.as_view(), name='foto_view'),
    path('foto/add/', PhotoCreateView.as_view(), name='foto_create')

]