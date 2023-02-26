from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def galeria(request):
    return HttpResponse('<h1>Alura Space</h1>')