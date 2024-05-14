from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=50 )
    desc=models.TextField(null=True, blank=True)
    rate=models.DecimalField(max_digits=4,decimal_places=3)
    views=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.title
    
    class Meta:
        # verbose_name= 'Book'
        ordering=['title']