# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
# Create your views here.

def homepage(request):
    if request.method=="GET":
        context={"title":"Musify"}
        return render(request,"persons/index.html",context)
    else:
        username=request.POST.get("username")
        return HttpResponseRedirect(reverse("posts:list",kwargs={"username":username}))