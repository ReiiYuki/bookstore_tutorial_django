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
