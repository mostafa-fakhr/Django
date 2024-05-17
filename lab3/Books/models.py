from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User



class Isbn(models.Model):
    isbnId = models.IntegerField()
    author_title = models.CharField(max_length=30)
    book_title = models.CharField(max_length=30)
    def __str__(self):
        return self.author_title
    
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) :
        return self.name
    def clean(self) -> None:
        if len(self.name) < 2:
            raise ValidationError('The minimum length of a category name is 2 characters ')
        return super().clean()



class Book(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    rate = models.DecimalField(max_digits=4, decimal_places=3)
    views = models.DecimalField(max_digits=10, decimal_places=2)
    isbn=models.OneToOneField(Isbn,on_delete=models.CASCADE,default=None)
    user = models.ForeignKey(User , on_delete=models.PROTECT ,default=None)
    category = models.ManyToManyField(Category)


 

    def __str__(self):
        return self.title

    def clean(self):
        if len(self.title) < 10:
            raise ValidationError("The length of a book title is between 10 & 50 characters ")
        return super().clean()


