from django.shortcuts import render,redirect
from .models import Book


def index(request):
    my_context = {
        'Books': Book.objects.all()
    }
    return render(request, 'Pages/index.html', context=my_context)



def book_details(request, *args, **kwrgs):
        id = kwrgs.get('book_id')
        book= Book.objects.get(id=id)
        my_context={
             'book':book
        }
        return render(request, 'Pages/index.html', context=my_context)


def book_delete(request, **kwrgs):
    id = kwrgs.get('book_id')
    book = Book.objects.get(id=id)
    if book:
        book.delete()
    return redirect(index)


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        rate = request.POST.get('rate')
        views = request.POST.get('views')

        book=Book(title=title,desc=description,rate=rate,views=views)
        book.save()
        return redirect(index)
    
    
    return render(request, 'Pages/CreateBook.html')


def book_edit(request, **kwargs):
    id = kwargs.get('book_id')
    book= Book.objects.get(id=id)
    
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.rate= float(request.POST.get('rate'))
        book.desc = request.POST.get('description')
        book.views = request.POST.get('views')
        
        book.save()        
        return redirect(index)
    
    my_context = {
        'book': book
    }
    return render(request, 'Pages/edit_book.html', context=my_context)

    