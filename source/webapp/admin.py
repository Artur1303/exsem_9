from django.contrib import admin
from webapp.models import Photo, Favorites

admin.site.register(Photo),
admin.site.register(Favorites)