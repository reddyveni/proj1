from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def telugu(request):
    return HttpResponse('this our telugu movie ')
def chan(request):
    return HttpResponse('<h1><marquee>chan is my fav friend and she is very helpful person in this world and she want to become a software engeineering and she always ........,,,,.,,</marquee></h1>')