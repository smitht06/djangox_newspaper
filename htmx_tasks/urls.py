from django.urls import path
from .views import TaskListView, TaskDeleteView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="display_tasks"),
    path("delete/<int:id>/", TaskDeleteView.as_view(), name="delete_task"),
    path("create/", TaskCreateView.as_view(), name="create_task")               
]
