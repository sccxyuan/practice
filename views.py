from django.http import HttpResponse
from django.shortcuts import render_to_response

def zhuye(request):
    return render_to_response('zhuye.html')
def hello(request):
    return HttpResponse('hello world')