from django.db import models
from django.utils import timezone

# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    time = models.DateTimeField(default=timezone.now)