from django.db import models
from mastodon import Mastodon

# Create your models here.

class MastodonUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    api_base_url = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    def get_mastodon(self):
        return Mastodon(
            client_id=self.client_id,
            client_secret=self.client_secret,
            access_token=self.access_token,
            api_base_url=self.api_base_url
        )