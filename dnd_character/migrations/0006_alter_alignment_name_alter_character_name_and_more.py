# Generated by Django 4.2.5 on 2023-11-11 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_character', '0005_alignment_alter_character_alignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alignment',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='characterclass',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
