import helloworld
from django.conf.urls import  include, url
from helloworld.views import book, books
from django.urls import path
from . import views
urlpatterns = [
        path('all/', views.books,name='books'),
         path('<int: book_id>/book/',views.book,name='book'),
    path('create/',views.create, name="create")
               ]
