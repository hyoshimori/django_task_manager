from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_tasks, name='list_tasks'),
    path('tasks/<int:task_id>/', views.task_details, name='task_details'),
    path('tasks/new/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),  # Updated this line
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),  # Updated this line
]
