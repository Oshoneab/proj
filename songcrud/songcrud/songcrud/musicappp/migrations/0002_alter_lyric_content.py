# Generated by Django 4.1.2 on 2022-10-28 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicappp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyric',
            name='content',
            field=models.TextField(max_length=20000),
        ),
    ]
