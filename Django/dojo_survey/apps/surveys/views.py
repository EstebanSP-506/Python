# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0
    return render(request, 'surveys/index.html')


def show(request):
    return render(request, 'surveys/result.html')


def process(request):
    if request.method == 'POST':
        request.session['counter'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
    return redirect('/result')


def reset(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
