from django.urls import path
from .views import books_list, book_details, upload_book


app_name="books"
urlpatterns = [
    path('', books_list, name="books_list"),
    path('<int:id>', book_details, name="book_details"),
    path('upload', upload_book, name="upload_book"),
]
