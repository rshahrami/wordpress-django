# Generated by Django 4.1.6 on 2023-03-11 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploadimage', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostModel',
            new_name='UploadImageModel',
        ),
    ]