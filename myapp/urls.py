from django.urls import path
from .views import index, about, login, contact, drivers, cars

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('drivers/', drivers, name='drivers'),
    path('cars/', cars, name='cars'),
    path('contact/<int:id>/', contact, name='contact'),
]