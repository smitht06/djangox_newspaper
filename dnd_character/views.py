from django.views.generic.edit import CreateView
from .models import Character
from .forms import CharacterCreationForm
from django.views.generic import ListView, DetailView


class CharacterCreateView(CreateView):
    model = Character
    form_class = CharacterCreationForm
    template_name = "dnd_character/character_create.html"  # Replace with your desired template
    success_url = ""  # Replace with the URL to redirect to after successful form submission

class CharacterListView(ListView):
    model = Character
    template_name = "dnd_character/character_list.html"

class CharacterDetailView(DetailView):
    model = Character
    template_name = "dnd_character/character_detail.html"
    