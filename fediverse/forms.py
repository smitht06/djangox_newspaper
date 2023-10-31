from django import forms

from .models import MastodonUser


class MastodonUserCreationForm(forms.ModelForm):
    class Meta:
        model = MastodonUser
        fields = [
            "username",
            "password",
            "client_id",
            "client_secret",
            "access_token",
            "api_base_url",
        ]

class MastodonUserUpdateForm(forms.ModelForm):
    class Meta:
        model = MastodonUser
        fields = [
            "username",
            "password",
            "client_id",
            "client_secret",
            "access_token",
            "api_base_url",
        ]
    


