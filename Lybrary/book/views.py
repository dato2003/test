from django.shortcuts import render
from .models import Book

def book_list(request):
   
    return render(request, 'book_list.html',)

