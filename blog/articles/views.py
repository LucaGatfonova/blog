from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Article


def article_list(request):
    article_list = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'article_list': article_list})


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article': article})
