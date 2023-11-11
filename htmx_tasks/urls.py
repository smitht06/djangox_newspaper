from django.urls import path
from .views import display_tasks, delete_task

urlpatterns = [
    path("", display_tasks, name="display_tasks"),
    path("delete/<int:id>/", delete_task, name="delete_task")               
]
