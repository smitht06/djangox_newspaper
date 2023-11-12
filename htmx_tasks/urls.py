from django.urls import path
from .views import create_task, TaskListView, TaskDeleteView

urlpatterns = [
    path("", TaskListView.as_view(), name="display_tasks"),
    path("delete/<int:id>/", TaskDeleteView.as_view(), name="delete_task"),
    path("create/", create_task, name="create_task")               
]
