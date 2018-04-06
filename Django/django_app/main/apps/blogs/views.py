# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    context = {
        "email": "poesteba@amazon.com",
        "name": "Esteban SP"
    }
    return render(request, "blog/index.html", context)


def new(request):
    response = "Hello, this is the path for a new article creation -- 'placeholder to display a new form to create a new blog'"
    return HttpResponse(response)


def create(request):
    response = "This is the path to handle the creation itself"
    print response
    return redirect('/')


def show(request, number):
    response = "Hello, this is the page for article number " + \
        str(number)+" --- placeholder to display blog "+str(number)
    return HttpResponse(response)


def edit(request, number):
    response = "This is the path to edit article number " + \
        str(number)+" --- placeholder to edit blog "+str(number)
    return HttpResponse(response)


def destroy(request, number):
    response = "Hello human, I am here to destroy article number " + \
        str(number)
    print response
    return redirect('/')
