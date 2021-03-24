from django.shortcuts import render


def index(request):
    return render(request, 'reviews/base.html')


def search_book(request):
    search_text = request.GET.get('search', '')
    return render(request, 'reviews/search-results.html', {'search_text': search_text})
