# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from persons.models import person

from .forms import Login_form

def homepage(request):
    if request.method=="GET":
        form = Login_form()
        context={"title":"Musify","login_form":form}
        return render(request,"persons/index.html",context)
    else:
        if request.POST.get('email'):
            print 'signup form'
        else:
            form=Login_form(request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
            context = {"title": "Musify", "login_form": form}
            return render(request, "persons/index.html", context)