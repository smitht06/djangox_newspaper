from django.urls import path
from .views import CharacterCreateView

urlpatterns = [
    # Other URL patterns...
    path("create/", CharacterCreateView.as_view(), name="character-create"),
]
