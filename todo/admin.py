from django.contrib import admin
from .models import Category, Todo
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name', 'user']
    search_fields = ['name']

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ['user', 'body', 'datetime', 'done']
    search_fields = ['user__username']
