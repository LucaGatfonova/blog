from django.shortcuts import render, HttpResponse


def article_list(request):
    article = 'Моя первая статья'
    return render(request, 'articles.html', {'article': article})
