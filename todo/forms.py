from django.db import models
from django.forms import fields
from .models import TodoList
from django import forms
from .models import TodoList


class ToDoForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'content']
