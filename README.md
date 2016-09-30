#Django Book Store Tutorial
##What you should know before start?
  1. In Django, you can iterate on data which you render on HTML.

    `views.py`
    ```Python
    def index(request) :
      bookstore = Book.objects.all()
      return render(request,'index.html',{'bookstore':bookstore})
    ```

    `index.html`
    ```html
    {% for book in bookstore %}
    <h1>{{book.name}}</h1>
    {% endfor %}
    ```

    Result
    ```
    Java Programming
    Python Programming
    ```

  2. In Django, you can use if-elif-else expression on your rendered HTML.

    ```html
    {% if book is not None %}
    {{book.name}}
    {% endif %}
    ```

  3. reverse() is use for simplify any URL on your app.

    With reverse()
    ```Python
    def redirect(request) :
      return HttpResponseRedirect('reverse('book:index')')
    ```
    ```Python
    app_name = 'book'
    urlpatterns = [
      url(r'book/index^$',views.index,name='index'),
    ]
    ```

    Without reverse()
    ```Python
    def redirect(request) :
      return HttpResponseRedirect('/book/index/')
    ```
    ```Python
    urlpatterns = [
      url(r'book/index^$',views.index),
    ]
    ```

  4. In Django you can work with Session on your request easily.

    ```python
    def session_test(request) :
      request.session['A'] = 9 # Create A field to session
      del request.session['A'] #destroy field A
    ```

##Let's Start!
  1. Initialize our project

    In your cmd, terminal, or bash...
    ```
    django-admin startproject bookstore
    cd bookstore
    ```

  2. Change Database Setting to use MySQL

    Edit `bookstore\settings.py` at DATABASES
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bookstore',
            'HOST' : 'localhost',
            'USER' : 'root',
            'PASSSWORD' : '',
            'PORT' : '3306'
        }
    }
    ```

  3. Initialize store app

    In your cmd, terminal, or bash...
    ```
    python manage.py startapp store
    ```

    Now, you will got `store` directory in your project

  4. Connect your app to your project

    Edit `bookstore\settings.py` at INSTALLED_APPS
    ```python
    INSTALLED_APPS = [
        'store.apps.StoreConfig', #ADD THIS LINE
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]
    ```

  5. Route your app to project.

    Create `store\urls.py`
    ```python
    from django.conf.urls import url

    from . import views

    app_name = 'store'

    urlpatterns = [

    ]
    ```

    Edit `bookstore\urls.py` to connect to your `store\urls.py`
    ```python
    from django.conf.urls import url,include
    from django.contrib import admin

    urlpatterns = [
        url(r'^',include('store.urls')),
        url(r'^admin/', admin.site.urls),
    ]
    ```

  6. Create Book Model in your store app

    Edit `store\models.py`
    ```python
    class Book(models.Model) :
      book_id = models.PositiveIntegerField(primary_key=True)
      isbn = models.PositiveIntegerField()
      book_name = models.CharField(max_length=200)
      price = models.FloatField()
      author = models.CharField(max_length=200)
    ```

    Migrate it to our database (Do this in your cmd)
    ```
    python manage.py makemigrations store
    python manage.py Migrate
    ```

  7. Make it show it webpage

    Create `store\templates\index.html` We will use this as our webpage.
    ```html
    <!Doctype html>
    <html>
      <header>
        <meta charset="utf-8">
        <title>Bookstore</title>
      </header>
      <body>
        <h1>Book Store</h1>
      </body>
    </html>
    ```

    Edit `store\views.py` to have a method to serve our webpage from index.html
    ```python
    from django.shortcuts import render

    # Create your views here.
    def index(request) :
        return render(request,'index.html')
    ```

    Edit `store\urls.py` to route your app to index method
    ```python
    from django.conf.urls import url

    from . import views

    app_name = 'store'

    urlpatterns = [
        url(r'^$',views.index,name='index'),
    ]
    ```

    Let's run server and go to `http://localhost:8000/` you will see what you wrote in your index.html  
    ```
    python manage.py runserver
    ```

  8. Create simple insert form.

    Add this part to body of your `store\templates\index.html` as the form that we will work on it.  
    ```html
    <h2>Insert New Book</h2>
    <form>
      Book ID : <input type="number">
      <br><br>
      ISBN : <input type="number">
      <br><br>
      Book Name : <input type="text">
      <br><br>
      Price : <input type="number">
      <br><br>
      Author : <input type="text">
      <br><br>
      <input type="submit" value="INSERT">
    </form>
    ```

    Let's run server and go to `http://localhost:8000/` you will see the simple insert form. However it doesn't work.
    ```
    python manage.py runserver
    ```

  9. Make our form work for inserting book.

    Before we work on our form let prepare some method to receive request from our form and it will be insert book to our database.  
    Edit `store\views.py` then add method to insert book  
    ```python
    from django.shortcuts import render
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    from .models import Book

    # Create your views here.
    def index(request) :
        return render(request,'index.html')

    def insert(request) :
        book_id = request.POST['book_id']
        isbn = request.POST['isbn']
        book_name = request.POST['book_name']
        price = request.POST['price']
        author = request.POST['author']
        book = Book.objects.create(book_id=book_id,isbn=isbn,book_name=book_name,price=price,author=author)
        book.save()
        return HttpResponseRedirect(reverse('store:index'))
    ```

    Next, we will create route to our insert method.
    Edit `store\urls.py` add this following line in urlpatterns
    ```python
    url(r'^insert/$',views.insert,name='insert'),
    ```

    After that let modify our form to interact with insert method.  
    Edit `store\templates\index.html` by  
    Add action to form which reference to our insert method url, then set method as POST because we will post the data to it.  
    Modify each input field to have name same as we define to receive in field of request.POST in insert method.    
    Don't forget to add `{% csrf_token %}` in your form, because it require for work on form with Django.  
    ```html
    <form action="{% url 'store:insert' %}" method="POST">
      {% csrf_token %}
      Book ID : <input type="number" name="book_id">
      <br><br>
      ISBN : <input type="number" name="isbn">
      <br><br>
      Book Name : <input type="text" name="book_name">
      <br><br>
      Price : <input type="number" name="price">
      <br><br>
      Author : <input type="text" name="author">
      <br><br>
      <input type="submit" value="INSERT">
    </form>
    ```

    Let's run server and go to `http://localhost:8000/` and try to insert some book.
    ```
    python manage.py runserver
    ```

    Then go to see your table in your database you will see your book is added to the schema.

  10. Create simple table for show list of book on it.

    Before we create the table, let's modify our `index` method in `store\views.py`　to make it able to send list of book to the webpage.
    ```python
    def index(request) :
        book_list = Book.objects.all()
        return render(request,'index.html',{'book_list':book_list})
    ```

    Add this following table to body of `store\templets\index.html`      
    You will see that I use for each iterating our book_list which we parse it in index method.
    ```html
    <table>
      <!-- table header -->
      <tr>
        <th>Book ID</th>
        <th>ISBN</th>
        <th>Book Name</th>
        <th>Price</th>
        <th>Author</th>
      </tr>
      <!-- iterating inserting row in table -->
      {% for book in book_list %}
        <tr>
          <td>{{ book.book_id }}</td>
          <td>{{ book.isbn }}</td>
          <td>{{ book.book_name }}</td>
          <td>{{ book.price }}</td>
          <td>{{ book.author }}</td>
        </tr>
      {% endfor %}
    </table>
    ```

    Let's run server and go to `http://localhost:8000/` and you will see that list of table is appeared.
    ```
    python manage.py runserver
    ```

  11. Make delete button to delete each book.

    First, we have to create one more method to handle delete action when request is comming in `store\views.py`.       
    Ps. we will delete it by id of it.
    ```python
    def delete(request) :
        book_id = request.POST['book_id']
        book = Book.objects.get(book_id=book_id)
        Book.delete(book)
        return HttpResponseRedirect(reverse('store:index'))
    ```

    Add this following line to urlpatterns in `store\urls.py` to make route to delete method
    ```python
    url(r'^delete/$',views.delete,name='delete'),
    ```

    Let's modify table in `store\templates\index.html` to have delete in each row.        
    However now we have only 5 columns, so we have to create one more empty header to represent to column of delete button.
    ```html
    <table>
      <!-- table header -->
      <tr>
        <th>Book ID</th>
        <th>ISBN</th>
        <th>Book Name</th>
        <th>Price</th>
        <th>Author</th>
        <th></th>
      </tr>
      <!-- iterating inserting row in table -->
      {% for book in book_list %}
        <tr>
          <td>{{ book.book_id }}</td>
          <td>{{ book.isbn }}</td>
          <td>{{ book.book_name }}</td>
          <td>{{ book.price }}</td>
          <td>{{ book.author }}</td>
          <td>
            <form action="{% url 'store:delete' %}" method="post">
              {% csrf_token %}
              <button name="book_id" value="{{ book.book_id }}">Delete</button>
            </form>
          </td>
        </tr>
      {% endfor %}
    </table>
    ```

    Let's run server and go to `http://localhost:8000/` and you will see delete buttons are appeared.
    ```
    python manage.py runserver
    ```

    If you press delete button it will delete those row from table and database.
