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
            ms.save()
            return HttpResponseRedirect('liuyanold.html')
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


def mendian(request):
      contact_list = Shop.objects.all()
      paginator = Paginator(contact_list, b) # Show 1 contacts per page
      try:
        page = int(request.GET.get('page', '1'))
      except ValueError:
        page = 1
      # If page request (9999) is out of range, deliver last page of results.
      try:
        contacts = paginator.page(page)
      except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
      return render_to_response('mendian.html', {"contacts": contacts})

def houqing(request):
        contact_list = Article.objects.all()
        paginator = Paginator(contact_list, b) # Show 1 contacts per page
        try:
          page = int(request.GET.get('page', '1'))
        except ValueError:
          page = 1
        try:
           contacts = paginator.page(page)
        except (EmptyPage, InvalidPage):
           contacts = paginator.page(paginator.num_pages)
        return render_to_response('houqing.html', {"contacts": contacts})
        

def news(request,new_id):
    contact_list = New.objects.all()
    paginator = Paginator(contact_list, a) # Show 1 contacts per page
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
              # If page request (9999) is out of range, deliver last page of results.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    p=New.objects.get(id=page)
    p.hoter=str(int(p.hoter)+1)
    p.save()
    return render_to_response('news.html', {"contacts": contacts})


def shop_detail(request,shop_id):
    contact_list = Shop.objects.all()
    paginator = Paginator(contact_list, a) # Show 1 contacts per page
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
          # If page request (9999) is out of range, deliver last page of results.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    p=Shop.objects.get(id=page)
    p.hoter=str(int(p.hoter)+1)
    p.save()
    
    return render_to_response('shop.html', {"contacts": contacts})
    


def article(request,article_id):
    contact_list = Article.objects.all()
    paginator = Paginator(contact_list, a) # Show 1 contacts per page
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
              # If page request (9999) is out of range, deliver last page of results.
    try:
        contacts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        contacts = paginator.page(paginator.num_pages)
    p=Article.objects.get(id=page)
    p.hoter=str(int(p.hoter)+1)
    p.save()
    return render_to_response('houqin.html', {"contacts": contacts})


