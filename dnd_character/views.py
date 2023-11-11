import random
from django.views.generic.edit import CreateView
from .models import Character
from .forms import CharacterCreationForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views import View
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CharacterCreateView(LoginRequiredMixin, CreateView):
    model = Character
    form_class = CharacterCreationForm
    template_name = "dnd_character/character_create.html"
    success_url = ""

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)


class CharacterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Character
    form_class = CharacterCreationForm
    template_name = "dnd_character/character_update.html"
    success_url = ""

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return obj.player == self.request.user


class CharacterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Character
    template_name = "dnd_character/character_delete.html"
    success_url = reverse_lazy("character_list")

    def test_func(self):
        obj = self.get_object()
        return obj.player == self.request.user


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


class CharacterListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Character
    template_name = "dnd_character/character_list.html"
    success_url = reverse_lazy("character_list")

    def test_func(self):
        obj = self.get_object()
        return obj.player == self.request.user


class CharacterDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Character
    template_name = "dnd_character/character_detail.html"

    def test_func(self):
        obj = self.get_object()
        return obj.player == self.request.user
