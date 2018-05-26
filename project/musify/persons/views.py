# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from django.contrib.auth import login
from .forms import Login_form,Registration_form

def homepage(request):
    if request.method=="GET":
        login_form = Login_form()
        registration_form = Registration_form()
        context={"title":"Musify","login_form":login_form,"registration_form":registration_form}

        return render(request,"persons/index.html",context)
    else:
        next=request.GET.get('next')
        if request.POST.get('email'):
            registration_form=Registration_form(request.POST)
            if registration_form.is_valid():
                instance=registration_form.save(commit=False)
                password=registration_form.cleaned_data.get('password')
                instance.set_password(password)
                instance.save()
                login(request,instance)
                redirect("/")
            context = {"title": "Musify","registration_form":registration_form,"login_form":Login_form()}
            return render(request, "persons/index.html", context)
        else:
            login_form=Login_form(request.POST)
            if login_form.is_valid():
                username=login_form.cleaned_data.get('username')
                password=login_form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
                login(request,user)
                if next:
                    return redirect(next)

            context = {"title": "Musify","registration_form":Registration_form(),"login_form":login_form}
            return render(request, "persons/index.html", context)
