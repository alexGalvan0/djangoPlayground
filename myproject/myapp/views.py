from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.p
def index(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Hello Wolrd</h1>')