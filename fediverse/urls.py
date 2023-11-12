from django.urls import path
from .views import (
    MastodonTimelineView,
    MastodonAddAccountView,
    MastodonUpdateAccountView,
    MastodonAccountDetailView,
)

urlpatterns = [
    path("", MastodonTimelineView.as_view(), name="mastodon_timeline"),
    path("create/", MastodonAddAccountView.as_view(), name="mastodon_add_account"),
    path(
        "account/<int:pk>",
        MastodonUpdateAccountView.as_view(),
        name="mastodon_account_update",
    ),
    path(
        "my_account/<int:pk>",
        MastodonAccountDetailView.as_view(),
        name="mastodon_account_detail",
    ),
]
