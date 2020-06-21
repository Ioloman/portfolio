from django.shortcuts import render
from .models import Article


def blog_main(request):
    articles = Article.objects.order_by('-date')[:5]
    return render(request, '../templates/blog/blog_main.html', {'articles': articles})
