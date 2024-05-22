from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic

from list.forms import TaskForm
from list.models import Task, Tag


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    context = {"tasks": tasks,
               "timezone": timezone,
               }
    return render(request, "list/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list:index")


class TagsList(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "list/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("list:tag-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    success_url = reverse_lazy("list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list:tag-list")


def toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("list:index")
