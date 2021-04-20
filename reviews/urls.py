from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/book-search/', views.book_search, name='book_search'),
    path('books/publishers/<int:pk>/', views.publisher_edit, name='publisher_edit'),
    path('books/publishers/new/', views.publisher_edit, name='publisher_create')
]
