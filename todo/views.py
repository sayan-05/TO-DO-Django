from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .forms import ToDoForm
from .models import TodoList
# Create your views here.


def home(request):
    data = TodoList.objects.all()
    context = {
        'data': data
    }
    return render(request, 'index.html', context)


def remove(request, user_id):
    item = TodoList.objects.get(id=user_id)
    item.delete()
    return redirect('/')


def create(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/')
    form = ToDoForm()
    context = {
        'form': form
    }

    return render(request, 'create.html', context)
