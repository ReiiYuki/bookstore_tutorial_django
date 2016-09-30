from django.conf.urls import url

from . import views

app_name = 'store'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^insert/$',views.insert,name='insert'),
    url(r'^delete/$',views.delete,name='delete'),
    url(r'^update/$',views.update,name='update'),
]
