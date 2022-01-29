from django.template.response import TemplateResponse
from .models import Book

def book_list_view(request):
    context ={}
    context["book_list"] = Book.objects.all()

    return TemplateResponse(request, "books/book_list.html", context)

def book_detail_view(request, pk):
    context = {}
    context["book"] = Book.objects.get(pk=pk)

    return TemplateResponse(request, "books/book_detail.html", context)
