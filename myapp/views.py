import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from myapp.forms import CarForm, ClientForm, DriverForm, EmployeeForm
from myapp.models import *

menu = [
    {'title': 'О сайте', 'url_name': 'myapp:about'},
    {'title': 'Машины парка', 'url_name': 'myapp:cars'},
    {'title': 'Водители парка', 'url_name': 'myapp:drivers'},
    {'title': 'Клиенты парка', 'url_name': 'myapp:clients'},
    {'title': 'Сотрудники', 'url_name': 'myapp:employee_list'}
    ]
def index(request):
    title = 'Главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/index.html', context=context)
def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/about.html', context=context)
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



def drivers(request):
    title = 'Водители парка'
    drivers = Driver.objects.all()
    context = {'title': title, 'menu': menu, 'drivers': drivers}
    return render(request, 'myapp/drivers.html', context=context)

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

def driver_card(request, pk):
    title='Информация о водителе'
    # client=Client.objects.get(pk=pk)
    driver = get_object_or_404(Driver, pk=pk)
    context={'title': title, 'menu': menu, 'driver': driver}

    return render(request, 'myapp/driver_card.html', context=context)

def cars(request):
    title = 'Машины парка'
    cars = Car.objects.all()
    context = {'title': title, 'menu': menu, 'cars': cars}
    return render(request, 'myapp/cars.html', context=context)

def add_car(request):
    title = 'Добавить машину'
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

    if request.method == "GET":
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)

def car_card(request, pk):
    title='Информация об автомобиле'
    # client=Client.objects.get(pk=pk)
    car = get_object_or_404(Car, pk=pk)
    context={'title': title, 'menu': menu, 'car': car}

    return render(request, 'myapp/car_card.html', context=context)

def clients(request):
    title = 'Клиенты парка'
    clients = Client.objects.all()
    context = {'title': title, 'menu': menu, 'clients': clients}
    return render(request, 'myapp/clients.html', context=context)

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

def client_card(request, pk):
    title='Информация о клиенте'
    # client=Client.objects.get(pk=pk)
    client = get_object_or_404(Client, pk=pk)
    context={'title': title, 'menu': menu, 'client': client}

    return render(request, 'myapp/client_card.html', context=context)

class EmployeeList(ListView):
    model = Employee
    template_name = 'myapp/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        # получение общего контекста из родительского класса
        context = super().get_context_data(**kwargs)
        # изменение родительского контекста (добавление ключей словаря)
        context['title'] = 'Сотрудники'
        context['count'] = Employee.objects.count()
        context['menu'] = menu
        return context

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'myapp/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        # получение общего контекста из родительского класса
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о сотруднике'
        context['menu'] = menu
        return context

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    # form_class = EmployeeForm
    template_name = 'myapp/employee_form.html'

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'myapp/employee_update.html'

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'myapp/employee_delete.html'
    success_url = reverse_lazy('employee_list')
