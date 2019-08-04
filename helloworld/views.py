# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from helloworld.models import Book
from django.shortcuts import redirect
from django.http import HttpResponse
from helloworld.forms import BookForm
from django.http import HttpResponseRedirect
#from django.core.context_processors import csrf
from django.template.context_processors import csrf



# Create your views here.
def books(request):
    return render_to_response('books.html',
                              {'books': Book.objects.all()}
                              )


def book(request, book_id=1):
    return render_to_response('book.html',
                              {'book': Book.objects.get(id=book_id)})
def create(request):
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/helloworld/all')
    else:
        form=BookForm()
    args={}
    args.update(csrf(request))
    args['form']=form
    return render_to_response("create_book.html", args)

