from django.shortcuts import render
from .forms import CarForm, DriverForm, ClientForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

from myapp.forms import CarForm, ClientForm, DriverForm
from myapp.models import Car

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Машины парка', 'url_name': 'cars'},
    {'title': 'Водители парка', 'url_name': 'drivers'},
    {'title': 'Клиенты парка', 'url_name': 'clients'},
    {'title': 'Войти', 'url_name': 'login'}
]
def index(request):
    title = 'Главная страница'
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
    car = Car.objects.all()
    context = {'title': title, 'menu': menu, 'cars': car}
    return render(request, 'myapp/cars.html', context=context)

def clients(request):
    title = 'Клиенты парка'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/clients.html', context=context)

@csrf_protect
def login(request):
    title = 'Войти'
    context = {'title': title, 'menu': menu}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f'Login - {username} Password - {password}')

    if request.method == 'GET':
        return render(request, 'myapp/login.html', context=context)

def contact(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name': name, 'age': age}
    return HttpResponse(f'Page contact, url_parametr_id = {url_id}, get_params = {get_params}')

def add_car(request):
    if request.method == "GET":
        title = 'Добавить машину'
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)
    if request.method == 'POST':
        carform = CarForm(request.POST)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
            car.save()
        return cars(request)

def add_client(request):

    title = 'Добавить клиента'

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return clients(request)
    else:
        form = ClientForm()

    context ={'title': title, 'menu': menu, 'form': form}
    return render(request, 'myapp/client_add.html', context=context)

def add_driver(request):

    title = 'Добавить водителя'

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return drivers(request)
    else:
        form = DriverForm()

    context ={'title': title, 'menu': menu, 'form': form}
    return render(request, 'myapp/driver_add.html', context=context)
