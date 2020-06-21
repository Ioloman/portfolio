from django.shortcuts import render


def homepage(request):
    return render(request, '../templates/portfolio_showcase/home.html')
