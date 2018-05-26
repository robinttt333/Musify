# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from persons.models import person

from .forms import Login_form,Registration_form

def homepage(request):
    if request.method=="GET":
        login_form = Login_form()
        registration_form = Registration_form()
        context={"title":"Musify","login_form":login_form,"registration_form":registration_form}
        return render(request,"persons/index.html",context)
    else:
        if request.POST.get('email'):
            registration_form=Registration_form(request.POST)
            if registration_form.is_valid():
                instance=registration_form.save(commit=False)
                password=registration_form.cleaned_data.get('passsword')
                instance.set_password(password)
                instance.save()
            context = {"title": "Musify","registration_form":registration_form,"login_form":Login_form()}
            return render(request, "persons/index.html", context)
        else:
            login_form=Login_form(request.POST)
            if login_form.is_valid():
                username=login_form.cleaned_data.get('username')
                password=login_form.cleaned_data.get('password')
            context = {"title": "Musify","registratio_form":Registration_form(),"login_form":login_form}
            return render(request, "persons/index.html", context)
