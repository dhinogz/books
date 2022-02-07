from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from .models import Book

@login_required
def book_list_view(request):
    context ={}
    context["book_list"] = Book.objects.all()

    return TemplateResponse(request, "books/book_list.html", context)

@login_required
def book_detail_view(request, pk):
    context = {}
    context["book"] = Book.objects.get(pk=pk)

    return TemplateResponse(request, "books/book_detail.html", context)
