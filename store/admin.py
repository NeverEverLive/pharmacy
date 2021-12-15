from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Position, Component, Drug, Employee, User, Supplier


@admin.register(Position)
class PositionAdmin(ModelAdmin):
    pass


@admin.register(User)
class PositionAdmin(ModelAdmin):
    pass


@admin.register(Employee)
class PositionAdmin(ModelAdmin):
    pass


@admin.register(Supplier)
class PositionAdmin(ModelAdmin):
    pass


@admin.register(Component)
class PositionAdmin(ModelAdmin):
    pass


@admin.register(Drug)
class PositionAdmin(ModelAdmin):
    pass