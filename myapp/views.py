from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>ABOUT site</h1>")

def login(request):
    return HttpResponse("<h2>LOGIN</h2>")

def contact(request):
    return HttpResponse("<h3>CONTACT</h3>")
