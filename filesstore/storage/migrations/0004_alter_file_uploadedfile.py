# Generated by Django 4.1 on 2022-08-12 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_file_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploadedFile',
            field=models.FileField(upload_to=models.CharField(max_length=200)),
        ),
    ]