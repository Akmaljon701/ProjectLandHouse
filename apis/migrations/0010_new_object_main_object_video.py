# Generated by Django 5.1.1 on 2024-09-16 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0009_application_applicationobject_applicationroom'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('video', models.TextField(verbose_name='URL-адрес видео')),
            ],
            options={
                'verbose_name': 'Новост',
                'verbose_name_plural': '7. Новости',
            },
        ),
        migrations.AddField(
            model_name='object',
            name='main',
            field=models.BooleanField(default=False, verbose_name='Основной объект'),
        ),
        migrations.AddField(
            model_name='object',
            name='video',
            field=models.TextField(default='https://www.youtube.com/embed/do7aB3efxiY?si=C1P0URBV6nueRakz', verbose_name='URL-адрес видео'),
            preserve_default=False,
        ),
    ]
