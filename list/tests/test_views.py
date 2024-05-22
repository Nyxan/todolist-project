from django.test import TestCase
from django.urls import reverse
from list.models import Task, Tag
from django.utils import timezone


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("list:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/index.html")


class TaskCreateViewTest(TestCase):
    def test_task_create_view(self):
        response = self.client.get(reverse("list:task-add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/task_form.html")


class TaskUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(content="Test Task", deadline=timezone.now())

    def test_task_update_view(self):
        response = self.client.get(reverse("list:task-update", args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/task_form.html")


class TaskDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(content="Test Task", deadline=timezone.now())

    def test_task_delete_view(self):
        response = self.client.get(reverse("list:task-delete", args=[self.task.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/task_confirm_delete.html")


class TagsListViewTest(TestCase):
    def test_tags_list_view(self):
        response = self.client.get(reverse("list:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/tag_list.html")


class TagCreateViewTest(TestCase):
    def test_tag_create_view(self):
        response = self.client.get(reverse("list:tag-add"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/tag_form.html")


class TagUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name="Test Tag")

    def test_tag_update_view(self):
        response = self.client.get(reverse("list:tag-update", args=[self.tag.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/tag_form.html")


class TagDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.tag = Tag.objects.create(name="Test Tag")

    def test_tag_delete_view(self):
        response = self.client.get(reverse("list:tag-delete", args=[self.tag.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list/tag_confirm_delete.html")


class ToggleStatusTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.task = Task.objects.create(content="Test Task", deadline=timezone.now())

    def test_toggle_status_view(self):
        response = self.client.get(reverse("list:toggle-status", args=[self.task.pk]))
        self.assertEqual(response.status_code, 302)
