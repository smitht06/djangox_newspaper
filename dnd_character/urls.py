from django.urls import path
from .views import (
    CharacterCreateView,
    CharacterListView,
    CharacterDetailView,
    GenerateRandomStatsView,
)

urlpatterns = [
    # Other URL patterns...
    path("create/", CharacterCreateView.as_view(), name="character_create"),
    path("", CharacterListView.as_view(), name="character_list"),
    path("<int:pk>/", CharacterDetailView.as_view(), name="character_detail"),
    path(
        "generate_random_stats/",
        GenerateRandomStatsView.as_view(),
        name="generate_random_stats",
    ),
]
