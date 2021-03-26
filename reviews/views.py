from django.shortcuts import render, get_object_or_404
from .models import Book
from .utils import average_rating


def books_list(request):
    books = Book.objects.filter(publication_date='2018-10-31')
    book_list = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        book_list.append({'book': book,
                          'book_rating': book_rating,
                          'number_of_reviews': number_of_reviews})
    context = {
        'book_list': book_list
    }
    return render(request, 'reviews/book_list.html', context)


def books_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = ({'book': book,
                    'book_rating': book_rating,
                    'reviews': reviews})

    else:
        context = ({'book': book,
                    'book_rating': None,
                    'reviews': None})

    return render(request, 'reviews/book_detail.html', context)


def books_publisher(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = ({'book': book,
                    'book_rating': book_rating,
                    'reviews': reviews})

    else:
        context = ({'book': book,
                    'book_rating': None,
                    'reviews': None})

    return render(request, 'reviews/book_detail.html', context)