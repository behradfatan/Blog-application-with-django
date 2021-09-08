from django.shortcuts import render, get_object_or_404
from .models import Article


def all_articles(request):
    all_articles = Article.objects.all()
    return render(request, "all_articles.html", {"all_articles": all_articles})

def article_detail(request, id, slug):
    # article = Article.objects.get(id=id, slug=slug)
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'article.html', {"article": article})