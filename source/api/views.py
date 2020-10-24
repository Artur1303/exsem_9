from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Photo, Favorites




class CreateView(APIView,):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        photo = get_object_or_404(Photo, pk=pk)
        created = Favorites.objects.get_or_create(photo=photo, author=request.user)
        if created:
            photo.save()
            return Response({'pk': pk})
        else:
            return Response(status=403)


class DeleteView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk=None):
        favorites = get_object_or_404(Favorites, pk=pk)
        favorites.delete()
        return Response({'pk': pk})

