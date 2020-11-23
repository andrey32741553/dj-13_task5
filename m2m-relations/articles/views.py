from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = '-published_at'
    article_list = Article.objects.all()
    context = {'object_list': article_list.order_by(ordering)}
    return render(request, template, context)
