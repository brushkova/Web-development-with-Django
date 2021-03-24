from django.shortcuts import render


def index(request):
    name = 'Kate'
    return render(request, 'reviews/base.html', {'name': name})
