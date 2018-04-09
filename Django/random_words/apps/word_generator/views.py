# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.


def index(request):
    rand_word = get_random_string(
        length=14, allowed_chars='ABCDEF0123456789')
    if 'counter' not in request.session:
        request.session['counter'] = 1
    context = {
        'counter': request.session['counter'],
        'word': rand_word,
    }
    return render(request, 'word_generator/index.html', context)


def show(request):
    request.session['counter'] += 1
    return redirect('/')


def reset(request):
    del request.session['counter']
    return redirect('/')
