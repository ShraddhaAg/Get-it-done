from django.urls import path
from . import views

urlpatterns = [
    path('', views.Task.as_view(), name='index'),
    path('/category', views.Category.as_view(), name='category'),
]
