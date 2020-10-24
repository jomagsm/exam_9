from django.contrib.auth import get_user_model
from django.db import models
# Фотография - картинка, обязательное;
# Подпись - строка, обязательное;
# Дата-время создания - проставляется автоматически;
# Автор - пользователь, обязательное


class Photo(models.Model):
    image = models.ImageField(upload_to='gallery_images', verbose_name='Фото')
    signature = models.CharField(max_length=200, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    author = models.ForeignKey(get_user_model(), null=True, blank=True, on_delete=models.CASCADE,
                             related_name='author_photo', verbose_name='Автор Фотографии')

    def __str__(self):
        return self.signature

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'