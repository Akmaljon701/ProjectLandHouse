# Generated by Django 5.1.1 on 2024-09-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0014_alter_application_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Заявка на общей информации', 'verbose_name_plural': '4. Заявка на общей информации'},
        ),
        migrations.AlterModelOptions(
            name='applicationobject',
            options={'verbose_name': 'Заявка об объекте', 'verbose_name_plural': '5. Заявка об объекте'},
        ),
        migrations.AlterModelOptions(
            name='applicationroom',
            options={'verbose_name': 'Заявка на комнату', 'verbose_name_plural': '6. Заявка на комнату'},
        ),
        migrations.AlterModelOptions(
            name='new',
            options={'verbose_name': 'Новост', 'verbose_name_plural': '7. Новости'},
        ),
        migrations.AlterModelOptions(
            name='objectblock',
            options={'verbose_name': 'Блок', 'verbose_name_plural': '3. Блоки'},
        ),
        migrations.AlterModelOptions(
            name='objectblockroom',
            options={'verbose_name': 'Комната объектов', 'verbose_name_plural': 'Объектные комнаты'},
        ),
        migrations.AlterModelOptions(
            name='objectphoto',
            options={'verbose_name': 'Фото объекта', 'verbose_name_plural': 'Фотографии объектов'},
        ),
        migrations.AddField(
            model_name='objectblock',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='objectblock',
            name='name_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Название'),
        ),
    ]
