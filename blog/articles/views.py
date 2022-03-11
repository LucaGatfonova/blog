from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Article
from .forms import LoginForm, UserRegistration, ArticleRegistrationForm
from django.contrib.auth import authenticate, login


def article_list(request):
    article_list = Article.objects.all().order_by('-published')
    return render(request, 'articles.html', {'article_list': article_list})


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'details.html', {'article': article})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                login(request, user)
                return HttpResponse("You are authenticated")

            else:
                return HttpResponse("Invalid Login")

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == "POST":
        user_form = UserRegistration(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            new_user.set_password(user_form.cleaned_data['password'])

            new_user.save()
            return render(request, 'account/register_done.html', {'user_form': user_form})

    else:
        user_form = UserRegistration()

    return render(request, 'account/register.html', {'user_form': user_form})


def article_form(request):
    if request.method == "POST":
        article_form = ArticleRegistrationForm(request.POST)

        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_list')

    else:
        article_form = ArticleRegistrationForm()

    return render(request, 'account/add_article.html', {'article_form': article_form})
