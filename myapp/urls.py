from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('drivers/', drivers, name='drivers'),
    path('cars/', cars, name='cars'),
    path('clients/', clients, name='clients'),
    path('contact/<int:id>/', contact, name='contact'),
    path('add_car/', add_car, name='add_car'),
    path('add_client/', add_client, name='add_client'),
    path('add_driver/', add_driver, name='add_driver'),

]