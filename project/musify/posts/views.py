# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect,reverse
from .forms import PostForm
# Create your views here.
from django.contrib.auth import get_user_model
from .models import Post
from django.contrib.auth.decorators import login_required

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.db.models import Q
User=get_user_model()

@login_required(login_url="/")
def list_view(request,username=None):
    q=request.GET.get('q')
    queryset_list=Post.objects.all()
    if q:
        queryset_list=queryset_list.filter(Q(title__icontains=q)|Q(lyrics__icontains=q)).distinct()
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "list": queryset,
        "username":username,
        "page_request_var": page_request_var
    }
    return render(request,'posts/list.html',context)

@login_required(login_url="/")
def create_view(request,username=None):
    form=PostForm(None or request.POST,None or request.FILES)
    if request.method=="GET":
        return render(request,'posts/create.html',{"username":username,"form":form})
    else:
        instance=form.save(commit=False)
        instance.author=User.objects.filter(username__iexact=username).first()
        instance.save()
        return redirect("/posts/"+username)



@login_required(login_url="/")
def details_view(request,username=None,id=None):
    obj=get_object_or_404(Post,id=id)
    return render(request,"posts/details.html",{"object":obj,"username":username})