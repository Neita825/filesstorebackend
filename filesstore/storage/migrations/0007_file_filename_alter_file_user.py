# Generated by Django 4.1 on 2022-08-12 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0006_alter_file_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='fileName',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
