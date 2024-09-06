# Generated by Django 5.1.1 on 2024-09-06 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_object_latitude_object_longitude_alter_object_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objects_count', models.PositiveIntegerField(verbose_name='Количество объектов')),
                ('clients', models.PositiveIntegerField(verbose_name='Доволеные клиенты')),
                ('years', models.PositiveIntegerField(verbose_name='Лет на рынке')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_uz', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Статистика компании',
                'verbose_name_plural': '1. Статистика компании',
            },
        ),
        migrations.AlterModelOptions(
            name='object',
            options={'verbose_name': 'Объект', 'verbose_name_plural': '1. Объекты'},
        ),
        migrations.AlterModelOptions(
            name='objectphoto',
            options={'verbose_name': 'Фото объекта', 'verbose_name_plural': '3. Фотографии объектов'},
        ),
        migrations.AlterModelOptions(
            name='objectroom',
            options={'verbose_name': 'Комната объектов', 'verbose_name_plural': '3. Объектные комнаты'},
        ),
    ]
