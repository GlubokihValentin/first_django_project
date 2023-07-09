from django.urls import path
from .views import index, about, login, contact

urlpatterns = [
    path('', index),
    path('about/', about),
    path('login/', login),
    path('contact/<int:id>/', contact),
]