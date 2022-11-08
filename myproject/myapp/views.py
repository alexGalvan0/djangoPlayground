from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Author, Book
from pprint import pprint as pp

# Create your views here.p


def index(request):
    if request.method == 'GET':
        authors = list(Author.objects.values())
        return JsonResponse({'data': authors})


def authors(request, id):
    if request.method == 'GET':
        authors = list(Book.objects.filter(id=id).values())
        return JsonResponse({'data': authors})

def authBook(request, name):
    if request.method == 'GET':
        authorId = list(Author.objects.filter(first_name = name))
        pp(authorId[0])

        books = list(Book.objects.filter(author = authorId[0].id).values())
        return JsonResponse({'data':books})
