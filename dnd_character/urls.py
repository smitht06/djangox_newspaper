from django.urls import path
from .views import CharacterCreateView, CharacterListView, CharacterDetailView

urlpatterns = [
    # Other URL patterns...
    path("create/", CharacterCreateView.as_view(), name="character_create"),
    path("", CharacterListView.as_view(), name="character_list"),
    path("<int:pk>/", CharacterDetailView.as_view(), name="character_detail"),
]
