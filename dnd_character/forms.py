from django import forms

from .models import Character


class CharacterCreationForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            "name",
            "race",
            "character_class",
            "level",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
            "max_hit_points",
            "current_hit_points",
            "alignment",
            "background",
            "personality_traits",
            "backstory",
        ]
