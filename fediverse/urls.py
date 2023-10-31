from django.urls import path
from .views import MastodonTimelineView

urlpatterns = [
    path("", MastodonTimelineView.as_view(), name="mastodon_timeline"),
]