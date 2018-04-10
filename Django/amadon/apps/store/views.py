# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    return redirect('/amadon')


def amadon(request):
    if 'products' not in request.session:
        request.session['total'] = 0
        request.session['items'] = 0
        request.session['products'] = [
            {
                'id': 1,
                'price': 19.99,
                'name': 'Dojo T-Shirt'
            },
            {
                'id': 2,
                'price': 29.99,
                'name': 'Dojo Sweater'
            },
            {
                'id': 3,
                'price': 4.99,
                'name': 'Dojo Cup'
            },
            {
                'id': 4,
                'price': 49.99,
                'name': 'Algorithm Book'
            },
            {
                'id': 5,
                'price': 1.99,
                'name': 'Vaseline'
            }
        ]
    return render(request, 'store/index.html')


def process(request):
    if request.method == 'POST':
        prod = request.POST
        for item in request.session['products']:
            if int(prod['product_id']) == item['id']:
                total = float(item['price'])*float(prod['quantity'])
                request.session['cart'] = {
                    'product_name': item['name'],
                    'quantity': prod['quantity'],
                    'product_price': item['price'],
                    'total_charged': total,
                }
                request.session['total'] += total
                request.session['items'] += int(prod['quantity'])
        request.session.modified = True
    return redirect('/amadon/checkout')


def checkout(request):
    return render(request, 'store/checkout.html')


def clear(request):
    request.session.clear()
    return redirect('/')
