from django.db import models
from apis import choices


class Object(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    name = models.CharField(
        max_length=300,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=50,
        choices=choices.ObjectStatuses.choices,
        default=choices.ObjectStatuses.IN_PROCESS
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"


class ObjectPhoto(models.Model):
    object_fk = models.ForeignKey(
        Object,
        related_name='photos',
        on_delete=models.CASCADE
    )

    photo = models.ImageField(
        upload_to='objects',
        blank=True,
        null=True,
        verbose_name="Фото"
    )

    class Meta:
        verbose_name = "Фото объекта"
        verbose_name_plural = "Фотографии объектов"

    def __str__(self):
        return self.object_fk.title

