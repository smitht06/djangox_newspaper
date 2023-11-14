from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import MastodonUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .bs import remove_links
from django.views.generic.edit import CreateView, UpdateView
from .forms import MastodonUserCreationForm, MastodonUserUpdateForm
from mastodon import Mastodon
from datetime import datetime


class MastodonTimelineView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    template_name = "fediverse/timeline.html"
    context_object_name = "mastodon_timeline"
    model = MastodonUser
    paginate_by = 5
    ids = []

    def get_template_names(self):
        if self.request.htmx:
            return "fediverse/timeline_partial.html"
        else:
            return "fediverse/timeline.html"

    def get_queryset(self):
        # with open("status.json", "a") as f:
        #     f.write(str(MastodonUser.objects.get(user=self.request.user).get_timeline()))
        return self.get_timeline(MastodonUser.objects.get(user=self.request.user))

    def test_func(self):
        return (
            self.request.user == MastodonUser.objects.get(user=self.request.user).user
        )

    def get_mastodon_api(self, mastodonUser):
        return Mastodon(
            client_id=mastodonUser.client_id,
            client_secret=mastodonUser.client_secret,
            access_token=mastodonUser.access_token,
            api_base_url=mastodonUser.api_base_url,
        )

    def get_timeline(self, mastodonUser):
        mastodon = self.get_mastodon_api(mastodonUser)
        timeline = mastodon.timeline_local(limit=50)
        timeline = self.clean_timeline(timeline)
        
        
        return timeline

    def clean_timeline(self, timeline):
        for status in timeline:
            status["content"] = remove_links(status["content"])
            if status["id"] in self.ids:
                timeline.remove(status)
            else:
                self.ids.append(status["id"])
        return timeline


class MastodonAddAccountView(CreateView, LoginRequiredMixin):
    model = MastodonUser
    form_class = MastodonUserCreationForm
    template_name = "fediverse/mastodonuser_create.html"
    success_url = ""

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MastodonUpdateAccountView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = MastodonUser
    form_class = MastodonUserUpdateForm
    template_name = "fediverse/mastodonuser_update.html"
    success_url = "../"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return (
            self.request.user == MastodonUser.objects.get(user=self.request.user).user
        )


class MastodonAccountDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = MastodonUser
    template_name = "fediverse/mastodonuser_detail.html"
    context_object_name = "mastodonuser"
