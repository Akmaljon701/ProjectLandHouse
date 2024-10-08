# Generated by Django 5.1.1 on 2024-09-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0010_new_object_main_object_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='new',
            name='description_uz',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='new',
            name='title_ru',
            field=models.CharField(max_length=300, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='new',
            name='title_uz',
            field=models.CharField(max_length=300, null=True, verbose_name='Заголовок'),
        ),
    ]
