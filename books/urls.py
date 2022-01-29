from django.contrib import admin 
from django.urls import path
from .views import book_detail_view, book_list_view

urlpatterns = [
    path('', book_list_view, name='book_list'),
    path('<uuid:pk>/', book_detail_view, name='book_detail'),
]
