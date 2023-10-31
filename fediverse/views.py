from django.shortcuts import render
from django.views.generic import ListView
from .models import MastodonUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .bs import remove_links
from django.views.generic.edit import CreateView
from .forms import MastodonUserCreationForm


# Create your views here.


class MastodonTimelineView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = "fediverse/timeline.html"
    context_object_name = "mastodon_timeline"
    model = MastodonUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mastodon_timeline"] = MastodonUser.objects.get(
            user=self.request.user
        ).get_timeline()
        return context

    def test_func(self):
        return (
            self.request.user == MastodonUser.objects.get(user=self.request.user).user
        )

class MastodonAddAccountView(CreateView):
    model = MastodonUser
    form_class = MastodonUserCreationForm
    template_name = "fediverse/mastodonuser_create.html"
    success_url = "/fediverse/timeline/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
