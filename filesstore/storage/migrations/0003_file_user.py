# Generated by Django 4.1 on 2022-08-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_rename_title_file_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='user',
            field=models.CharField(default='admin', max_length=200),
        ),
    ]