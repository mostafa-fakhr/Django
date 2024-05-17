from django.shortcuts import render,redirect
from .models import Book,Category,Isbn
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@login_required(login_url='/user/login')
def index(request):
    my_context = {
        'Books': Book.objects.all()
    }
    return render(request, 'Pages/index.html', context=my_context)


@login_required(login_url='/user/login')
def book_details(request, *args, **kwrgs):
        id = kwrgs.get('book_id')
        book= Book.objects.get(id=id)
        my_context={
             'book':book
        }
        return render(request, 'Pages/index.html', context=my_context)

@login_required(login_url='/user/login')
def book_delete(request, **kwrgs):
    id = kwrgs.get('book_id')
    book = Book.objects.get(id=id)
    if book:
        book.delete()
    return redirect(index)

@login_required(login_url='/user/login')
def add_book(request):
    categories = Category.objects.all()
    isbns = Isbn.objects.all()
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        rate = request.POST.get('rate')
        isbn_id = request.POST.get('isbn')
        category_id = request.POST.get('category')
        views = request.POST.get('views')

        category = Category.objects.get(id=category_id)
        isbn = Isbn.objects.get(id=isbn_id)
        
        user = request.user

        book = Book.objects.create(title=title, desc=description, rate=rate, views=views, isbn=isbn, user=user)
        
        book.category.add(category)
        
        return redirect('BookStore_index')

    return render(request, 'Pages/CreateBook.html', {'categories': categories, 'isbns': isbns})


@login_required(login_url='/user/login')
@csrf_protect
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

    