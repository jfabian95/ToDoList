from django.contrib import admin
from django.urls import path
from .views import home, todolist,delete_todo

urlpatterns = [
    path('', home, name="Home"),
    path('todolist', todolist, name="todolist"),
    path('delete_todo/<int:todo_id>', delete_todo, name="delte_todo"),
]
