from django.db import models
from apis import choices


class Company(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название"
    )
    phone = models.CharField(
        max_length=13,
        verbose_name="Телефон"
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Электронная почта"
    )
    you_tube = models.URLField(
        blank=True,
        null=True,
        verbose_name="Ютуб"
    )
    instagram = models.URLField(
        blank=True,
        null=True,
        verbose_name="Инстаграм"
    )
    telegram = models.URLField(
        blank=True,
        null=True,
        verbose_name="Телеграм"
    )
    facebook = models.URLField(
        blank=True,
        null=True,
        verbose_name="Фейсбук"
    )
    objects_count = models.PositiveIntegerField(
        verbose_name="Количество объектов"
    )
    clients = models.PositiveIntegerField(
        verbose_name="Доволеные клиенты"
    )
    years = models.PositiveIntegerField(
        verbose_name="Лет на рынке"
    )
    address = models.CharField(
        max_length=300,
        blank=True,
        null=True,
        verbose_name="Адрес"
    )
    longitude = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Долгота",
    )
    latitude = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Широта"
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание",
    )

    class Meta:
        verbose_name = "Статистика компании"
        verbose_name_plural = "1. Статистика компании"


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
        blank=True,
        null=True,
        verbose_name="Описание",
    )
    status = models.CharField(
        max_length=50,
        choices=choices.ObjectStatuses.choices,
        default=choices.ObjectStatuses.IN_PROCESS,
        verbose_name="Статус",
    )
    longitude = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Долгота",
    )
    latitude = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Широта"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "2. Объекты"


class ObjectPhoto(models.Model):
    object_fk = models.ForeignKey(
        Object,
        related_name='photos',
        on_delete=models.CASCADE,
        verbose_name="Объект"
    )

    photo = models.ImageField(
        upload_to='objects',
        blank=True,
        null=True,
        verbose_name="Фото"
    )

    class Meta:
        verbose_name = "Фото объекта"
        verbose_name_plural = "3. Фотографии объектов"


class ObjectRoom(models.Model):
    object_fk = models.ForeignKey(
        Object,
        related_name='rooms',
        on_delete=models.CASCADE,
        verbose_name="Объект"
    )

    photo = models.ImageField(
        upload_to='rooms',
        blank=True,
        null=True,
        verbose_name="Фото"
    )
    total_area = models.FloatField(
        verbose_name="Общая площадь"
    )
    block = models.CharField(
        max_length=50,
        verbose_name="Блок"
    )
    count = models.PositiveIntegerField(
        verbose_name="Количество комнат"
    )
    floor = models.PositiveIntegerField(
        verbose_name="Этаж"
    )
    entrance = models.PositiveIntegerField(
        verbose_name="Подъезд"
    )
    price = models.FloatField(
        verbose_name="Цена"
    )
    status = models.CharField(
        max_length=50,
        choices=choices.ObjectRoomStatuses.choices,
        default=choices.ObjectRoomStatuses.NOT_SOLD,
        verbose_name="Статус",
    )

    class Meta:
        verbose_name = "Комната объектов"
        verbose_name_plural = "3. Объектные комнаты"




