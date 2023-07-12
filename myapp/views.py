import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from myapp.forms import CarForm, ClientForm, DriverForm
from myapp.models import Car, Client, Driver

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Машины парка', 'url_name': 'cars'},
    {'title': 'Водители парка', 'url_name': 'drivers'},
    {'title': 'Клиенты парка', 'url_name': 'clients'},
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
    drivers = Driver.objects.all()
    context = {'title': title, 'menu': menu, 'drivers': drivers}
    return render(request, 'myapp/drivers.html', context=context)

def cars(request):
    title = 'Машины парка'
    cars = Car.objects.all()
    context = {'title': title, 'menu': menu, 'cars': cars}
    return render(request, 'myapp/cars.html', context=context)

def clients(request):
    title = 'Клиенты парка'
    clients = Client.objects.all()
    context = {'title': title, 'menu': menu, 'clients': clients}
    return render(request, 'myapp/clients.html', context=context)

@csrf_protect
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f'Login: {username} Password: {password}')

    title = 'Войти'
    context = {'title': title, 'menu': menu}

    if request.method == 'GET':
        return render(request, 'myapp/login.html', context=context)

def contact(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name': name, 'age': age}
    return HttpResponse(f'Page contact, url_parametr_id = {url_id}, get_params = {get_params}')

def add_car(request):
    title = 'Добавить машину'
    if request.method == "GET":
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            # car = Car()
            # car.brand = form.cleaned_data['brand']
            # car.model = form.cleaned_data['model']
            # car.color = form.cleaned_data['color']
            # car.power = form.cleaned_data['power']
            # car.year = form.cleaned_data['years']
            form.save()
            return cars(request)

def add_client(request):

    title = 'Добавить клиента'

    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            age = datetime.date.today().year - form.cleaned_data['birthday'].year
            instance.age = age
            instance.save()
            form.save()
            return clients(request)
    else: #request.method == 'GET'
        form = ClientForm()
        context ={'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/client_add.html', context=context)

def add_driver(request):

    title = 'Добавить водителя'

    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return drivers(request)
    else:
        form = DriverForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/driver_add.html', context=context)
