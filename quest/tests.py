from django.test import TestCase
from django.urls import reverse

from quest import forms


class TestForms(TestCase):
    def test_not_valid_question_form(self):
        form = forms.QuestionForm({'title': 'Title', 'question': 'How to make money?'})
        self.assertFalse(form.is_valid())

    def test_valid_answer_acceptance_form(self):
        form = forms.AnswerAcceptanceForm({'accepted': False})
        self.assertTrue(form.is_valid())

    def test_not_valid_answer_form(self):
        form = forms.AnswerForm({})
        self.assertFalse(form.is_valid())


class TestViews(TestCase):
    def test_index(self):
        response = self.client.get(reverse('quest:index'))
        self.assertEqual(302, response.status_code)
