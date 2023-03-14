from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def giri(request):
    return HttpResponse('<marquee><h1>giri is good boy</h1></marquee>')
def Nithin(request):
    return HttpResponse('<marquee><h1>Nithin is very innocent</h1></marquee>')