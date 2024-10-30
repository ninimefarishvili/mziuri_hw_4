from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.

def home(request):
    books = Book.objects.all()
    ctx = {"books": books}

    return render(request, "base.html", context=ctx)

def create_book(request):
    bookForm = BookForm()

    if request.method == "POST":
        bookForm = BookForm(request.POST)
        if bookForm.is_valid():
            bookForm.save()
            return redirect("home")
    return render(request, 'book_create.html', context={'form': bookForm})

def detail_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, "detail_book.html", context={"book": book})

def delelte_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()

    return redirect("home")



def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=pk)  
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})
