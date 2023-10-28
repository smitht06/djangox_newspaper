from django.views.generic.edit import CreateView
from .models import Character
from .forms import CharacterCreationForm


class CharacterCreateView(CreateView):
    model = Character
    form_class = CharacterCreationForm
    template_name = "dnd_character/character_create.html"  # Replace with your desired template
    success_url = ""  # Replace with the URL to redirect to after successful form submission
