from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    object_list = Article.objects.select_related('author').select_related('genre')
    ordering = '-published_at'
    context = {'object_list': object_list.order_by(ordering)}
    return render(request, template_name, context)
