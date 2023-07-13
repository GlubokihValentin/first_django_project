from django import forms
from django.forms import ModelForm
from .models import *
import datetime
from firstproject.settings import DATE_INPUT_FORMAT
def year_choices():
    return [(r, r) for r in range(1970, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class CarForm(ModelForm):
    class Meta:
        model = Car
        # exclude = ['age']
        fields = '__all__'

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        # exclude = ['last_name']
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['age']
        # fields = ['name', 'last_name']

    birthday = forms.DateField(input_formats=DATE_INPUT_FORMAT, label='Дата рождения')