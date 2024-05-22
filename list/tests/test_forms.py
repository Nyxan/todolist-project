from django.test import TestCase
from list.forms import TaskForm
from list.models import Tag


class TaskFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='Test Tag 1')
        Tag.objects.create(name='Test Tag 2')

    def test_task_form_valid_data(self):
        form_data = {
            'content': 'Test Task Content',
            'deadline': '2024-05-22T12:00',
            'tags': [tag.pk for tag in Tag.objects.all()]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_invalid_data(self):
        form_data = {
            'content': '',
            'deadline': '2024-05-22T12:00',
            'tags': [tag.pk for tag in Tag.objects.all()]
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_form_missing_deadline(self):
        form_data = {
            'content': 'Test Task Content',
            'tags': [tag.pk for tag in Tag.objects.all()]
        }
        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_task_form_empty_tags(self):
        form_data = {
            'content': 'Test Task Content',
            'deadline': '2024-05-22T12:00',
            'tags': []
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_task_form_invalid_tags(self):
        form_data = {
            'content': 'Test Task Content',
            'deadline': '2024-05-22T12:00',
            'tags': [100, 200]
        }
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
