from django.urls import path
from .views import (
    CharacterCreateView,
    CharacterListView,
    CharacterDetailView,
    GenerateRandomStatsView,
    CharacterUpdateView,
    CharacterDeleteView,
)

urlpatterns = [
    # Other URL patterns...
    path("create/", CharacterCreateView.as_view(), name="character_create"),
    path("update/<int:pk>/", CharacterUpdateView.as_view(), name="character_update"),
    path("", CharacterListView.as_view(), name="character_list"),
    path("<int:pk>/", CharacterDetailView.as_view(), name="character_detail"),
    path(
        "generate_random_stats/",
        GenerateRandomStatsView.as_view(),
        name="generate_random_stats",
    ),
    path("delete/<int:pk>/", CharacterDeleteView.as_view(), name="character_delete"),
]
