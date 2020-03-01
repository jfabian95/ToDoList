from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo

def home(request):
    queryset = Todo.objects.all()
    context = {
        "todolist": queryset
    }

    return render(request, 'todos/todolist.html',context)

def todolist(request):
    todo = request.POST.get('todo')
    Todo.objects.create(entry=todo)
    
    return redirect('/')

def delete_todo(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    print(todo_id)
    return redirect('/')