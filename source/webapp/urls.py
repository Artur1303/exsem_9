from django.urls import path
from webapp.views import IndexView, PhotoView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', PhotoView.as_view(), name='foto_view'),

]