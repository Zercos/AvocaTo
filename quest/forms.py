from django import forms
from django.contrib.auth import get_user_model

from quest.models import Answer, Question


class AnswerForm(forms.ModelForm):
    user = forms.ModelChoiceField(get_user_model().objects.all(), widget=forms.HiddenInput, disabled=True)
    question = forms.ModelChoiceField(Question.objects.all(), widget=forms.HiddenInput, disabled=True)

    class Meta:
        model = Answer
        fields = ['answer', 'user', 'question', ]


class AnswerAcceptanceForm(forms.ModelForm):
    accepted = forms.BooleanField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Answer
        fields = ['accepted']


class QuestionForm(forms.ModelForm):
    user = forms.ModelChoiceField(get_user_model().objects.all(), widget=forms.HiddenInput, disabled=True)

    class Meta:
        model = Question
        fields = ['title', 'question', 'user', ]
