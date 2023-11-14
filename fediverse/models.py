from django.db import models
from mastodon import Mastodon
from django.conf import settings
import re
from utils.template_utils import remove_links
from datetime import datetime


# Create your models here.


class MastodonUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    api_base_url = models.CharField(max_length=100)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return "mastodon username: " + self.username



    
