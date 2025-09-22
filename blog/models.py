from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Содержимое")
    image = models.ImageField(
        upload_to="images/", null=True, blank=True, verbose_name="Изображение"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(verbose_name="Признак публикации")
    counter = models.IntegerField(verbose_name="Количество просмотров")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["title", "created_at"]
