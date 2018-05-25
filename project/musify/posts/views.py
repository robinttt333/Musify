# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from .forms import PostForm
# Create your views here.
from persons.models import person
from .models import Post

def list_view(request,username=None):
    query_list=Post.objects.all()
    context={"list":query_list,"username":username}
    return render(request,'posts/list.html',context)


def create_view(request,username=None):
    form=PostForm(None or request.POST,None or request.FILES)
    if request.method=="GET":
        return render(request,'posts/create.html',{"username":username,"form":form})
    else:
        instance=form.save(commit=False)
        instance.author=username
        instance.save()

def details_view(request,username=None,id=None):
    obj=get_object_or_404(Post,id=id)
    return render(request,"posts/details.html",{"object":obj,"username":username})