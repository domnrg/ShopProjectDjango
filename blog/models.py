from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Содержимое")
    image = models.ImageField(
        upload_to="images/", null=True, blank=True, verbose_name="Изображение"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Признак публикации")
    counter = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]
