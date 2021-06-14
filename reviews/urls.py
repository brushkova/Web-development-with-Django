from django.urls import path
from . import views, api_views

urlpatterns = [
    path('api/contributors/', api_views.ContributorView.as_view(), name='contributors'),
    path('api/all_books/', api_views.AllBooks.as_view(), name='all_books'),
    path('books/', views.BookList.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('books/book-search/', views.BookSearchList.as_view(), name='book_search'),
    path('books/publishers/new/', views.PublisherCreate.as_view(), name='publisher_create'),
    path('books/publishers/<int:pk>/', views.PublisherEdit.as_view(), name='publisher_edit')
   ]
