from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from list.forms import TaskForm
from list.models import Task, Tag


def index(request):
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    context = {"tasks": tasks}
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
