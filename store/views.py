from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Book

# Create your views here.
def index(request) :
    book_list = Book.objects.all()
    try :
        book = Book.objects.get(book_id=request.session['book_id_update'])
        del request.session['book_id_update']
    except KeyError :
        book = None
    return render(request,'index.html',{'book_list':book_list,'update_book':book})

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

def update(request) :
    try :
        book = Book.objects.get(book_id=request.POST['book_id_update'])
        book.book_id = request.POST['book_id']
        book.isbn = request.POST['isbn']
        book.book_name = request.POST['book_name']
        book.price = request.POST['price']
        book.author = request.POST['author']
        book.save()
    except KeyError :
        request.session['book_id_update'] = request.POST['book_id_update']
    return HttpResponseRedirect(reverse('store:index'))
