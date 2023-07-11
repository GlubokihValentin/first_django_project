from django.db import models

# 1. Create your models here
# 2. Create migrations: python manage.py makemigrations
# 3. Migrate: python manage.py migrate

class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    age = models.IntegerField(verbose_name="Возраст")
    city = models.CharField(max_length=100, verbose_name="Город")
    is_activated = models.BooleanField(verbose_name="Активация")

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

    def __str__(self):
        return ' '.join([str(self.name), str(self.city)])

class Car(models.Model):
    brand = models.CharField(max_length=30, verbose_name="Бренд")
    model = models.CharField(max_length=30, verbose_name="Модель")
    color = models.CharField(max_length=30, verbose_name="Цвет")
    power = models.IntegerField(verbose_name="Мощность")
    years = models.IntegerField(verbose_name="Год выпуска")

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self):
        return ' '.join([str(self.brand), str(self.model)])

class Client(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='День рождения')
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=30, verbose_name='Город')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Эл. почта')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return ' '.join([str(self.name), str(self.last_name)])
