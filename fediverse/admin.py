from django.contrib import admin

# Register your models here.

from .models import MastodonUser

admin.site.register(MastodonUser)