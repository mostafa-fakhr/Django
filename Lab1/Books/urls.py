from django.urls import path
from Books import views


urlpatterns = [
    path('', views.index, name='BookStore_index'),
    path('AddBook/',views.add_book,name='add-book'),
    path('book_details/<int:book_id>', views.book_details, name='book-details'),
    path('book_delete/<int:book_id>', views.book_delete, name='book-delete'),
    path('book_edit/<int:book_id>', views.book_edit, name='book-Edit'),

]