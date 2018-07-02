# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .form import accessForm
from .models import detail


# Create your views here.
def index(request):
    template = loader.get_template('app/form.html')
    context = {

    }
    return HttpResponse(template.render(context,request))


def access(request):
    if request.method == 'POST':
        access_form = accessForm(data=request.POST)
        print access_form.errors,access_form.is_valid()
        #print("hello");
        if access_form.is_valid():
           access_form.save()
           name = access_form.cleaned_data['employee_id']
           #id = request.POST.get('id', '')
           print(name)
           return render(request,"app/contact.html")
    return render(request, "app/form.html")

def admin(request):
    a = detail.objects.all()
    template = loader.get_template('app/admin.html')
    context = {
                      'data': a,
                      }
    output = template.render(context,request)
    return HttpResponse(output)
