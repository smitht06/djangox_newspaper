from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.

from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=50)

    # Add any additional race-specific fields here

    def __str__(self):
        return self.name


class CharacterClass(models.Model):
    name = models.CharField(max_length=50)

    # Add any additional class-specific fields here

    def __str__(self):
        return self.name


class Character(models.Model):
    # Basic Information
    name = models.CharField(max_length=255)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    character_class = models.ForeignKey(CharacterClass, on_delete=models.CASCADE)
    level = models.PositiveIntegerField(default=1)
    photo = models.ImageField(upload_to="media/character_photos", blank=True)

    # Ability Scores
    strength = models.PositiveIntegerField(default=10)
    dexterity = models.PositiveIntegerField(default=10)
    constitution = models.PositiveIntegerField(default=10)
    intelligence = models.PositiveIntegerField(default=10)
    wisdom = models.PositiveIntegerField(default=10)
    charisma = models.PositiveIntegerField(default=10)

    # Hit Points
    max_hit_points = models.PositiveIntegerField(default=10)
    current_hit_points = models.PositiveIntegerField(default=10)

    # Other Character Details
    alignment = models.CharField(max_length=20)
    background = models.CharField(max_length=50)
    personality_traits = models.TextField(blank=True)
    backstory = models.TextField(blank=True)

    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("character_detail", kwargs={"pk": self.pk})
