# Generated by Django 4.2.5 on 2023-11-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_character', '0002_character_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='photo',
            field=models.ImageField(blank=True, upload_to='character_photos'),
        ),
    ]
