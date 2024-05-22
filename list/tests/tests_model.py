from django.test import TestCase
from list.models import Tag, Task
from django.utils import timezone


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Test Tag')

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Test Tag')
        Task.objects.create(content='Test Task', deadline=timezone.now())

    def test_content_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_created_at_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('created_at').verbose_name
        self.assertEqual(field_label, 'created at')

    def test_deadline_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('deadline').verbose_name
        self.assertEqual(field_label, 'deadline')

    def test_is_done_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('is_done').verbose_name
        self.assertEqual(field_label, 'is done')

    def test_tags_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('tags').verbose_name
        self.assertEqual(field_label, 'tags')

    def test_content_max_length(self):
        task = Task.objects.get(id=1)
        max_length = task._meta.get_field('content').max_length
        self.assertEqual(max_length, None)  # No max_length set explicitly

    def test_deadline_null(self):
        task = Task.objects.get(id=1)
        self.assertIsNotNone(task.deadline)

    def test_is_done_default(self):
        task = Task.objects.get(id=1)
        self.assertFalse(task.is_done)