from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import AddTodoForm
from .models import ToDo


def index(request):
    return render(request, 'todo/index.html')


def add_todo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddTodoForm()
            value = request.POST['value']
            print(value)

            new_todo = ToDo.objects.create(name=request.user, value=value)
        else:
            form = AddTodoForm()
        return render(request, 'todo/add_todo.html', {'form' : form})
    else:
        return HttpResponseRedirect('../../you_are_logged_in/')


def my_todo(request):
    if request.user.is_authenticated:
        get_user = request.user
        my_todo = ToDo.objects.filter(name=get_user, status=True).order_by('date_add')

        if len(my_todo) == 0:
            message = 'you have 0 todo item'
        else:
            message = None
        return render(request, 'todo/my_todo.html', {
            'my_todo': my_todo,
            'message': message,
            
            })
    else:
        return HttpResponseRedirect('../../you_are_logged_in/')


def delete_todo(request, todo_id):
    ToDo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('../../my_todo/')


def you_are_loged_in(request):
    return render(request, 'todo/logged_in.html')