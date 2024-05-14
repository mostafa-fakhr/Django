from django.shortcuts import render,redirect

Books=[
  {
    'id':1,
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
    "price": 9.99,
    "published_date": "1960-07-11",
    "description": "To Kill a Mockingbird is a novel by Harper Lee published in 1960. It was immediately successful, winning the Pulitzer Prize, and has become a classic of modern American literature.",
    "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQzIxlL18J8kPtAJd90BEaH6kIG7HXNo0OS3ztKxDkig1Noj53lbwGEUfQgyTMA9ZdKdcg&usqp=CAU"
  },
  {
    'id':2,
    "title": "1984",
    "author": "George Orwell",
    "genre": "Science Fiction",
    "price": 12.99,
    "published_date": "1949-06-08",
    "description": "1984 is a dystopian novel by George Orwell, published in 1949. It is set in a future where the government, under the Party, monitors and controls everything, suppressing dissent and manipulating the truth.",
    "image":"https://www.penguinreaders.co.uk/wp-content/uploads/2020/04/9780241430972-667x1024.jpg"
  },
  {
    'id':3,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Fiction",
    "price": 11.99,
    "published_date": "1925-04-10",
    "description": "The Great Gatsby is a novel by American author F. Scott Fitzgerald, first published in 1925. The story is set in the summer of 1922 and follows the life of Jay Gatsby, a wealthy man who throws extravagant parties in the hope of rekindling his romance with Daisy Buchanan.",
    "image":"https://miro.medium.com/v2/resize:fit:500/0*R__G0x9FqfzO-pei.jpg"
  },
  {
    'id':4,
    "title": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "genre": "Fantasy",
    "price": 14.99,
    "published_date": "1997-06-26",
    "description": "Harry Potter and the Philosopher's Stone is the first novel in the Harry Potter series written by J.K. Rowling. The book follows the journey of a young wizard, Harry Potter, who discovers his magical heritage on his eleventh birthday when he receives a letter of acceptance to the Hogwarts School of Witchcraft and Wizardry.",
    "image":"https://m.media-amazon.com/images/I/71RVt35ZAbL._AC_UF1000,1000_QL80_.jpg"
  },
  {
    'id':5,
    "title": "The Catcher in the Rye",
    "author": "J.D. Salinger",
    "genre": "Fiction",
    "price": 10.49,
    "published_date": "1951-07-16",
    "description": "The Catcher in the Rye is a novel by J.D. Salinger, first published in 1951. The story is a first-person narrative of a young man named Holden Caulfield, who describes his experiences and interactions with others during a few days in December 1949.",
    "image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeBNFt_j2SbKCeIRC7Vv4yDi4_SaTx8fX6kWTpqWd6Sw&s"
  }
]

def index(request):
    my_context = {
        'Books': Books
    }
    return render(request, 'Pages/index.html', context=my_context)


def _get_book(book_id):
    for book in Books:
        if 'id' in book and book['id'] == book_id:
            return book
    return None

def book_details(request, *args, **kwrgs):
        id = kwrgs.get('book_id')
        book=_get_book(id)
        my_context={
             'book':book
        }
        return render(request, 'Pages/book_details.html', context=my_context)


def book_delete(request, **kwrgs):
    id = kwrgs.get('book_id')
    book = _get_book(id)
    if book:
        Books.remove(book)
    return redirect(index)


def add_book(request):
    if request.method == 'POST':
       
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        image = request.POST.get('image')
        price = float(request.POST.get('price'))
        published_date = request.POST.get('published_date')
        description = request.POST.get('description')
        
        new_book = {
            'id': len(Books) + 1, 
            'title': title,
            'author': author,
            'genre': genre,
            'price': price,
            'published_date': published_date,
            'description': description,
            'image':image
        }
        Books.append(new_book)

        return redirect(index)
    
    
    return render(request, 'Pages/CreateBook.html')


def book_edit(request, **kwargs):
    id = kwargs.get('book_id')
    book = _get_book(id)

    print(id)
    
    if request.method == 'POST':
        book['title'] = request.POST.get('title')
        book['author'] = request.POST.get('author')
        book['genre'] = request.POST.get('genre')
        book['price'] = float(request.POST.get('price'))
        book['published_date'] = request.POST.get('published_date')
        book['description'] = request.POST.get('description')
        
        for index, item in enumerate(Books):
            if item['id'] == id:
                Books[index] = book
                break
        
        return redirect(book_details, book_id=id)
    
    my_context = {
        'book': book
    }
    return render(request, 'Pages/edit_book.html', context=my_context)

    