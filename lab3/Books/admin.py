from django.contrib import admin
from .models import Book,Category,Isbn
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = [ 'title','rate' , 'views' , 'isbn' , 'category' ]
admin.site.register(Book,BookAdmin)
admin.site.site_header="BookStore"



admin.site.register(Category)
admin.site.register(Isbn)