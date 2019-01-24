from django.shortcuts import render
from tasks.models import task, hashtag
from django.views import generic

class Task(generic.ListView):
    model = task

class Category(generic.ListView):
    model = hashtag

class TaskDetail(generic.DetailView):
    model = task

class CategoryDetail(generic.DetailView):
    model = hashtag
