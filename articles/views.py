from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Article
from django.urls import reverse_lazy


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "articles/article_detail.html"
    context_object_name = "article"


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ("title", "body")
    template_name = "articles/article_edit.html"


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/article_delete.html"
    success_url = reverse_lazy("article_list")


class ArticleCreateView(CreateView):
    model = Article
    template_name = "articles/article_new.html"
    fields = (
        "title",
        "body",
        "author",
    )
