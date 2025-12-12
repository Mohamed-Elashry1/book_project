from django.shortcuts import render, redirect
from .models import Book
from .forms import UploadBookForm
# Create your views here.



def books_list(request):
    books = Book.objects.all()
    context = {
        "books": books,
        "page_title": "E-book | All books"
    }
    return render(request, 'books_list.html', context)


def book_details(request, **kwargs):
    book = Book.objects.get(id=kwargs['id'])
    context = {
        "page_title":f"{book.title}",
        "book":book
    }
    return render(request, 'book_details.html', context)    



def upload_book(request):
    if request.method == "POST":
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid:
            book = form.save()
            return redirect('books:book_details', id=book.id)
    else:
        form = UploadBookForm()
    context = {
        "form": form,
        "page_title": "E-book | Uploade books"
    }
    return render(request, 'upload_book.html', context)