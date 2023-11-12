from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from .models import MastodonUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .bs import remove_links
from django.views.generic.edit import CreateView, UpdateView
from .forms import MastodonUserCreationForm, MastodonUserUpdateForm


# Create your views here.


class MastodonTimelineView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = "fediverse/timeline.html"
    context_object_name = "mastodon_timeline"
    model = MastodonUser
    paginate_by = 10

    def get_queryset(self):
        return MastodonUser.objects.get(user=self.request.user).get_timeline()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def test_func(self):
        return (
            self.request.user == MastodonUser.objects.get(user=self.request.user).user
        )

    def get_paginated_timeline(self):
        queryset = self.get_queryset()
        paginator = Paginator(queryset, self.paginate_by)
        page_number = self.request.GET.get("page")
        page = paginator.get_page(page_number)
        return page

    def render_to_response(self, context, **reponse_kwargs):
        if self.request.headers.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            page = self.get_paginated_timeline()
            posts_html = render_to_string(
                "fediverse/timeline.html",
                {"mastodon_timeline": page, "request": self.request},
            )
            return JsonResponse({"html": posts_html, "has_next": page.has_next()})
        else:
            return super().render_to_response(context, **reponse_kwargs)

class MastodonAddAccountView(CreateView, LoginRequiredMixin):
    model = MastodonUser
    form_class = MastodonUserCreationForm
    template_name = "fediverse/mastodonuser_create.html"
    success_url = "fediverse/"

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
