# Generated by Django 4.2.5 on 2023-11-01 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_character', '0003_character_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='photo',
            field=models.ImageField(blank=True, upload_to='media/character_photos'),
        ),
    ]
