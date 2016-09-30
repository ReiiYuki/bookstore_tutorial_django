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

    Add this part to body of your `store\templates\index.html`
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
