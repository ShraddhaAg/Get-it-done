from django.shortcuts import render
from tasks.models import task, hashtag
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class Task(generic.ListView):
    model = task

class Category(generic.ListView):
    model = hashtag

class TaskDetail(generic.DetailView):
    model = task

class CategoryDetail(generic.DetailView):
    model = hashtag

class HashtagCreate(CreateView):
    model = hashtag
    fields = '__all__'
    success_url = reverse_lazy('category')

class TaskCreate(CreateView):
    model = task
    fields = '__all__'
    success_url = reverse_lazy('task')
