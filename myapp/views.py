from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Main Page</h1>")
def about(request):
    return HttpResponse("<h1>ABOUT site</h1>")

def login(request):
    return HttpResponse("<h2>LOGIN</h2>")

def contact(request, id):
    name = request.GET.get('name')
    age = request.GET.get('age')
    return HttpResponse(f'Page contact, id={id}, name={name}, age={age}')
