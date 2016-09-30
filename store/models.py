from django.db import models

# Create your models here.
class Book(models.Model) :
    book_id = models.PositiveIntegerField(primary_key=True)
    isbn = models.PositiveIntegerField()
    book_name = models.CharField(max_length=200)
    price = models.FloatField()
    author = models.CharField(max_length=200)
