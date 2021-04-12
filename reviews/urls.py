from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('books/base-form/', views.view_function, name='base_form'),
]
