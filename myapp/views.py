from django.shortcuts import render
from django.http import HttpResponse

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Машины парка', 'url_name': 'cars'},
    {'title': 'Водители парка', 'url_name': 'drivers'},
    # {'title': 'Клиенты', 'url_name': 'clients'},
]
def index(request):
    title = 'Main home page'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/index.html', context=context)
def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/about.html', context=context)

def drivers(request):
    title = 'Водители парка'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/drivers.html', context=context)

def cars(request):
    title = 'Машины парка'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/cars.html', context=context)

def login(request):
    return HttpResponse("<h2>LOGIN</h2>")

def contact(request, id):
    name = request.GET.get('name')
    age = request.GET.get('age')
    return HttpResponse(f'Page contact, id={id}, name={name}, age={age}')



