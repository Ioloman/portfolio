from django.shortcuts import render
from .models import Portfolio_DB


def homepage(request):
    objects = Portfolio_DB.objects.all()
    return render(request, '../templates/portfolio_showcase/home.html', {'portfolios': objects, 'title': 'Portfolio'})
