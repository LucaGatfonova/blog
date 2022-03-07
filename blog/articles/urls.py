from django.urls import path
from .views import article_list, article_details

urlpatterns = [
    path('', article_list, name='article_list'),
    path('articles/<slug:slug>/', article_details, name='article_details'),
]
