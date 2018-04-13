# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.


def index(request):
    return render(request, 'users/index.html', {'users': User.objects.all()})


def new(request):
    return render(request, 'users/new_user.html')


def create(request):
    if request.method == 'POST'
        dataPOST = request.POST
        new_user = User.objects.create(
            first_name=str(dataPOST['first_name']), last_name=str(dataPOST['last_name']), email=str(dataPOST['email']))
        return redirect("/users/"+str(new_user.id))
    return redirect("/users/")


def edit(request, user_id):
    context = {'user_data': User.objects.get(id=user_id)}
    return render(request, 'users/edit_user.html', context)


def show(request, user_id):
    context = {'user_data': User.objects.get(id=user_id)}
    return render(request, 'users/show_user.html', context)


def update(request):
    if request.method == 'POST'
        dataPOST = request.POST
        user = User.objects.get(id=dataPOST['user_id'])
        user.first_name = dataPOST['first_name']
        user.last_name = dataPOST['last_name']
        user.email = dataPOST['email']
        user.save()
        return redirect("/users/"+str(dataPOST['user_id']))
    return redirect("/users/")


def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("/users")
