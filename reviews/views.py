from django.shortcuts import render, get_object_or_404

from .forms import OrderForm, SearchForm
from .models import Book, Contributor
from .utils import average_rating


def index(request):
    return render(request, "reviews/base.html")


def form_example(request):

    if request.method == "POST":
        form = OrderForm(request.POST)
    else:
        form = OrderForm()

    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))

    return render(request, "reviews/base_form.html", {"method": request.method, "form": form})


def book_search(request):
    search_text = request.GET.get("search", "")
    form = SearchForm(request.GET)
    form_2 = SearchForm(request.GET)
    books = set()
    if form.is_valid() and form.cleaned_data["search"]:
        search = form.cleaned_data["search"]
        search_in = form.cleaned_data.get("search_in") or "title"
        if search_in == "title":
            books = Book.objects.filter(title__icontains=search)
        else:
            fname_contributors = Contributor.objects.filter(first_names__icontains=search)
            for contributor in fname_contributors:
                for book in contributor.book_set.all():
                    books.add(book)

        lname_contributors = Contributor.objects.filter(last_names__icontains=search)

        for contributor in lname_contributors:
            for book in contributor.book_set.all():
                books.add(book)

    return render(request, "reviews/search_results.html", {"form": form, "search_text": search_text, "books": books,
                                                           "form_2": form_2})


def book_list(request):
    books = Book.objects.all()
    books_with_reviews = []
    for book in books:
        reviews = book.review_set.all()
        if reviews:
            book_rating = average_rating([review.rating for review in reviews])
            number_of_reviews = len(reviews)
        else:
            book_rating = None
            number_of_reviews = 0
        books_with_reviews.append({"book": book, "book_rating": book_rating, "number_of_reviews": number_of_reviews})

    context = {
        "book_list": books_with_reviews
    }
    return render(request, "reviews/book_list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = book.review_set.all()
    if reviews:
        book_rating = average_rating([review.rating for review in reviews])
        context = {
            "book": book,
            "book_rating": book_rating,
            "reviews": reviews
        }
    else:
        context = {
            "book": book,
            "book_rating": None,
            "reviews": None
        }
    return render(request, "reviews/book_detail.html", context)
