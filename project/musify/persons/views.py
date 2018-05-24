# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
# Create your views here.
from persons.models import person
def homepage(request):
    if request.method=="GET":
        context={"title":"Musify"}
        return render(request,"persons/index.html",context)
    else:
        username=request.POST.get("username")
        obj=person(username=username).save()
        return HttpResponseRedirect(reverse("posts:list",kwargs={"username":username}))