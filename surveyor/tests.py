from django.test import TestCase
from unittest import skip

from .views import new_question
from .models import Question


class QuestionViewsTest(TestCase):
    def test_new_question_form(self):
        resp = self.client.get('/question/new/')
        self.assertTrue('form' in resp.context)

    def test_creates_new_question(self):
        start_count = Question.objects.count()
        data = {'text': 'some test question'}
        self.client.post('/question/new/', data)
        self.assertEqual(Question.objects.count() - start_count, 1)

    def test_doesnt_create_new_question_if_invalid(self):
        start_count = Question.objects.count()
        self.client.post('/question/new/', {})
        self.assertEqual(Question.objects.count() - start_count, 0)
