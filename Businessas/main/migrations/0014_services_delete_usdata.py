# Generated by Django 4.1 on 2023-01-29 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_usdata_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=1000, verbose_name='Номер услуги')),
                ('title', models.CharField(max_length=1000, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('price', models.CharField(max_length=1000, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Раздел услуги',
                'verbose_name_plural': 'Раздел услуги',
            },
        ),
        migrations.DeleteModel(
            name='UsData',
        ),
    ]
