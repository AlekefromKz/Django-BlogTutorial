from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Aleke home</h1>')

def experience(request):
    return HttpResponse('<h1>Aleke experience</h1>')
