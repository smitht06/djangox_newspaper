from django.shortcuts import render
from .models import Task
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, View


class TaskDeleteView(View):
    def delete(self, request, id):
        Task.objects.get(id=id).delete()
        tasks = Task.objects.all()
        return render(request, "htmx_tasks/tasks_list.html", {"tasks": tasks})
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
class TaskListView(ListView):
    model = Task
    template_name = "htmx_tasks/display_tasks.html"
    context_object_name = "tasks"


class TaskCreateView(View):
    def post(self, request):
        title = request.POST.get("title")
        Task.objects.create(title=title)
        tasks = Task.objects.all()
        return render(request, "htmx_tasks/tasks_list.html", {"tasks": tasks})
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)







