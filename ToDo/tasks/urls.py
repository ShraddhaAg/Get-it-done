from django.urls import path
from . import views

urlpatterns = [
    # path('', name='index'),
    path('task', views.Task.as_view(), name='task'),
    path('category', views.Category.as_view(), name='category'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('category/create/', views.HashtagCreate.as_view(), name='create-category'),
    path('task/create/', views.TaskCreate.as_view(), name='create-task'),
]
