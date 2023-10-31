from django.contrib.auth.models import AbstractUser
from django.db import models
from fediverse.models import MastodonUser


class CustomUser(AbstractUser):
    mastodon_account = models.ForeignKey(
        MastodonUser, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.username
