from django.shortcuts import render, get_object_or_404
from .models import Article


def blog_main(request):
    articles = Article.objects.order_by('-date')
    return render(request, '../templates/blog/blog_main.html', {'articles': articles, 'title': 'Blog'})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Article, pk=blog_id)
    return render(request, '../templates/blog/blog_detail.html', {'blog': blog, 'title': 'Article - ' + str(blog.title)})
