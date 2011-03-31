from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template,Context,TemplateDoesNotExist
from django.template.loader import get_template as get_Template
import datetime
from django import forms
from mysite.forms import ContactForm
from mysite.list.models import Article,New,Shop,Message
from django.core.paginator import Paginator, InvalidPage, EmptyPage
a=1
b=4
def zhuye(request):
    return render_to_response('1.html')

def hello(request):
    return HttpResponse('hello world')

def lianxi(request):
    return render_to_response('lianxi.html')

def jianjie(request):
    return render_to_response('jianjie.html')
    

def liuyan(request):
    if request.method=='post':
        form=ContactForm(request.POST)
        if form.is_valid():
            ct=form.cleaned_date
            ms=Message(sub=ct['sub'],content=ct['content'],name=ct['name'],contact=ct['contact'],email=ct['email'],)
            ms.save
            return HttpResponseRedirect('seeliuyan.html')
    else:
        form=ContactForm(initial={'sub':'I love you site.'})
    return render_to_response('liuyan.html',{'form':form})

def liuyanold(request):
    contact_list = Message.objects.all()
    paginator = Paginator(contact_list, b) 
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('liuyanold.html', {"contacts": contacts})