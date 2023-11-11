from django.shortcuts import render
from .models import Task
from django.views.decorators.http import require_http_methods

def display_tasks(request):
    tasks = Task.objects.all()
    return render(request, "htmx_tasks/display_tasks.html", {"tasks": tasks})

@require_http_methods(["DELETE"])
def delete_task(request, id):
    Task.objects.get(id=id).delete()
    tasks = Task.objects.all()
    return render(request, "htmx_tasks/tasks_list.html", {"tasks": tasks})

@require_http_methods(["POST"])
def create_task(request):
    title = request.POST.get("title")
    description = request.post.get("description")
    completed = request.POST.get("completed")
    Task.objects.create(title=title, description=description, completed=completed)
    tasks = Task.objects.all()
    return render(request, "htmx_tasks/create_task.html", {"tasks": tasks})




