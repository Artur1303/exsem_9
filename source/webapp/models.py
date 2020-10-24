from django.contrib.auth.models import User
from django.db import models



class Photo(models.Model):
    image = models.ImageField(upload_to='gallery-images', null=True,  verbose_name='Фото')
    signature = models.CharField(max_length=200, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    author = models.ForeignKey(User, max_length=50, verbose_name='Автор', related_name='photos_author',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.signature

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'