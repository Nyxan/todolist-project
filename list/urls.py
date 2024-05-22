from django.urls import path

from list.views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagsList,
    TagCreateView,
    TagsUpdateView,
    TagDeleteView,
    toggle_status)


urlpatterns = [
    path("", index, name="index"),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tags/', TagsList.as_view(), name='tag-list'),
    path('tags/add/', TagCreateView.as_view(), name='tag-add'),
    path('tag/<int:pk>/update/', TagsUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
    path('toggle/<int:pk>/', toggle_status, name='toggle-status'),
]

app_name = "list"
