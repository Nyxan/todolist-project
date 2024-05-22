from django.urls import path

from list.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,)


urlpatterns = [
    path("", index, name="index"),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]

app_name = "list"
