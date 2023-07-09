from django.db import models

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