# Generated by Django 4.1.2 on 2022-10-31 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicappp', '0002_alter_lyric_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='Song',
            new_name='song_id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='Artiste',
            new_name='artiste_id',
        ),
    ]
