from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book

# Create your views here.
def index(request) :
    book_list = Book.objects.all()
    return render(request,'index.html',{'book_list':book_list})

def insert(request) :
    book_id = request.POST['book_id']
    isbn = request.POST['isbn']
    book_name = request.POST['book_name']
    price = request.POST['price']
    author = request.POST['author']
    book = Book.objects.create(book_id=book_id,isbn=isbn,book_name=book_name,price=price,author=author)
    book.save()
    return HttpResponseRedirect(reverse('store:index'))

def delete(request) :
    book_id = request.POST['book_id']
    book = Book.objects.get(book_id=book_id)
    Book.delete(book)
    return HttpResponseRedirect(reverse('store:index'))
