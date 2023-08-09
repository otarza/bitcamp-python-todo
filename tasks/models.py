from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='tasks')


    def __str__(self):
        return self.title
