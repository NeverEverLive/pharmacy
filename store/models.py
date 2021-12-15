from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return f'ID: {self.id}: {self.name}'


class User(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING,  null=True)


class Supplier (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)


class Component(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class Drug(models.Model):
    name = models.CharField(max_length=70)
    components = models.ManyToManyField(Component)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'ID {self.id}: {self.name}'
