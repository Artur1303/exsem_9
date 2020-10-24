from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models



class Photo(models.Model):
    image = models.ImageField(upload_to='gallery-images', null=True,  verbose_name='Фото')
    signature = models.CharField(max_length=200, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    author = models.ForeignKey(User, max_length=50, verbose_name='Автор', related_name='photos_author',
                               on_delete=models.CASCADE)

    def liked_by(self, user):
        likes = self.favorite_photo.filter(author=user)
        return likes.count() > 0

    def __str__(self):
        return self.signature

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'


class Favorites(models.Model):
    photo = models.ForeignKey(Photo, related_name='favorite_photo', verbose_name='Фото', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), related_name='favorite_author',
                               verbose_name='Автор', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'