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



@require_http_methods(["POST"])
def create_task(request):
    title = request.POST.get("title")
    description = request.post.get("description")
    completed = request.POST.get("completed")
    Task.objects.create(title=title, description=description, completed=completed)
    tasks = Task.objects.all()
    return render(request, "htmx_tasks/create_task.html", {"tasks": tasks})




