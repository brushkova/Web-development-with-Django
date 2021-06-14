from django.db.models import Q
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.generic.edit import FormMixin
from .forms import PublisherForm, ReviewForm
from .models import Book, Publisher
from .utils import average_rating


def index(request):
    return render(request, "base.html")


class BookList(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'reviews/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books_with_reviews = []

        for book in self.get_queryset():
            reviews = book.review_set.all()
            if reviews:
                book_rating = average_rating([review.rating for review in reviews])
                number_of_reviews = len(reviews)
            else:
                book_rating = None
                number_of_reviews = 0

            books_with_reviews.append(
                {"book": book, "book_rating": book_rating, "number_of_reviews": number_of_reviews}
            )

        context.update({
            "book_list": books_with_reviews
        })

        return context


class BookSearchList(generic.ListView):
    model = Book
    template_name = 'reviews/search_results.html'
    context_object_name = 'book_list'

    def get_queryset(self):
        search = self.request.GET.get('search')
        object_list = Book.objects.all()
        if search:
            object_list = object_list.filter(Q(title__icontains=search) | Q(publisher__name__icontains=search))
        return object_list


@method_decorator(login_required, name='dispatch')
class PublisherCreate(generic.FormView):
    form_class = PublisherForm
    template_name = 'reviews/instance_form.html'

    def form_valid(self, form):
        form.save(self.request.user)
        return super(PublisherCreate, self).form_valid(form)

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO, "Publisher was created")
        return reverse('publisher_create')


@method_decorator(login_required, name='dispatch')
class PublisherEdit(generic.UpdateView):
    model = Publisher
    template_name = 'reviews/instance_form.html'
    form_class = PublisherForm

    def get_object(self, *args, **kwargs):
        publisher = get_object_or_404(Publisher, pk=self.kwargs['pk'])
        return publisher

    def get_success_url(self):
        messages.add_message(self.request, messages.INFO,
                             "Publisher \"{}\" was updated.".format(self.get_object().name))
        return reverse('publisher_edit',
                       kwargs={'pk': self.get_object().id}
                       )


@method_decorator(login_required, name='dispatch')
class BookDetail(FormMixin, generic.DetailView):
    model = Book
    context_object_name = 'book_detail'
    template_name = 'reviews/book_detail.html'
    form_class = ReviewForm

    def get_success_url(self):
        return reverse('book_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BookDetail, self).get_context_data(**kwargs)
        book = self.get_object()
        reviews = book.review_set.all()

        book_rating = average_rating([review.rating for review in reviews])
        context.update({
                "book": book,
                "book_rating": book_rating if reviews else None,
                "reviews": reviews if reviews else None,
                    })

        context['form'] = ReviewForm(initial={'book': self.object})
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.book = self.object
        review.creator = self.request.user
        review.save()
        return super(BookDetail, self).form_valid(form)
