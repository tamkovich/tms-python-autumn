from django.views.generic import ListView, DetailView

from home.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles.html"
    ordering = "title"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article.html"
    slug_field = "pk"
    context_object_name = "obj"
