from django.contrib import admin
from .models import ToDo


class ToDoIndex(admin.ModelAdmin):
    list_display = ['date_add', 'name', 'value', 'status']


admin.site.register(ToDo, ToDoIndex)
