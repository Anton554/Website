# Generated by Django 4.1 on 2023-01-29 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_usdata_fname_usdata_chapter_tx_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usdata',
            old_name='chapter_tx',
            new_name='chapter',
        ),
        migrations.RenameField(
            model_name='usdata',
            old_name='qweasdzxc',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='usdata',
            old_name='title_tx',
            new_name='title',
        ),
    ]
