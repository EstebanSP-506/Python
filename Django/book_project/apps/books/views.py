# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.


def index(request):
    context = {"authors": Author.objects.all()}
    return render(request, 'books/index.html', context)
