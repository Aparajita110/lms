from django.shortcuts import get_object_or_404, redirect, render
from.models import Book
from.forms import BookForm

def index(request):
    books =Book.objects.all()
    return render(
        request,
        'books/index.html',
        {
            'books': books
        }
    )



def view(request, id):
    book =get_object_or_404(Book,pk=id)
    return render(
        request,
        'books/detail.html',
        {
            'book':book
        }
    )


def create(request):
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(
        request,
        'books/create.html',
        {
            'form': form
        }
      )
    