from django.shortcuts import render
from .models import Article


def all_articles(request):
    all_articles = Article.objects.all()
    return render(request, "all_articles.html", {"all_articles": all_articles})
