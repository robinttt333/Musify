# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import PostForm
# Create your views here.

def list(request,username=None):
    return render(request,'posts/base.html',{"username":username})


def create(request,username=None):
    form=PostForm()
    return render(request,'posts/create.html',{"username":username,"form":form})

