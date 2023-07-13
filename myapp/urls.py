from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('cars/<int:pk>/', car_card, name='car_card'),
    path('cars/', cars, name='cars'),
    path('drivers/<int:pk>/', driver_card, name='driver_card'),
    path('drivers/', drivers, name='drivers'),
    path('clients/<int:pk>/', client_card, name='client_card'),
    path('clients/', clients, name='clients'),
    path('contact/<int:id>/', contact, name='contact'),
    path('add_car/', add_car, name='add_car'),
    path('add_driver/', add_driver, name='add_driver'),
    path('add_client/', add_client, name='add_client'),
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('employees_form/', EmployeeCreate.as_view(), name='employee_create'),


]