# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import datetime

# Create your views here.


def index(request):
    if 'words' not in request.session:
        request.session['words'] = []
        print 'new session'
    return render(request, 'words/index.html')


def add(request):
    if request.method == 'POST':
        now = datetime.datetime.now().strftime('%I:%M:%S %p, %B %d %Y')
        print request.POST
        request.session['words'].append((request.POST, str(now)))
        request.session.modified = True
        return redirect('/')


def clear(request):
    request.session.clear()
    return redirect('/')
