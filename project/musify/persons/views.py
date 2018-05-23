# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    context={"title":"Musify"}
    return render(request,"persons/index.html",context)