# Generated by Django 5.1.1 on 2024-09-06 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_alter_object_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='object',
            options={'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты'},
        ),
        migrations.AlterModelOptions(
            name='objectphoto',
            options={'verbose_name': 'Фото объекта', 'verbose_name_plural': 'Фотографии объектов'},
        ),
    ]
