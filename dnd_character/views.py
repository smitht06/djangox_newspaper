import random
from django.views.generic.edit import CreateView
from .models import Character
from .forms import CharacterCreationForm
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import JsonResponse


class CharacterCreateView(CreateView):
    model = Character
    form_class = CharacterCreationForm
    template_name = (
        "dnd_character/character_create.html"  # Replace with your desired template
    )
    success_url = (
        ""  # Replace with the URL to redirect to after successful form submission
    )

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)


class GenerateRandomStatsView(View):
    def get(self, request, *args, **kwargs):
        random_stats = self.generate_random_stats()
        return JsonResponse(random_stats)

    def generate_random_stats(self):
        stats = {}
        stats["strength"] = random.randint(3, 18)
        stats["dexterity"] = random.randint(3, 18)
        stats["constitution"] = random.randint(3, 18)
        stats["intelligence"] = random.randint(3, 18)
        stats["wisdom"] = random.randint(3, 18)
        stats["charisma"] = random.randint(3, 18)
        return stats


class CharacterListView(ListView):
    model = Character
    template_name = "dnd_character/character_list.html"


class CharacterDetailView(DetailView):
    model = Character
    template_name = "dnd_character/character_detail.html"
