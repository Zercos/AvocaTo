from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest
from django.urls import reverse
from django.utils import timezone
from django.views.generic import (CreateView, DayArchiveView, DetailView,
                                  RedirectView)

from quest.forms import AnswerAcceptanceForm, AnswerForm, QuestionForm
from quest.models import Question


class AskQuestionView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    template_name = 'quest/ask.html'

    def get_initial(self):
        return {'user': self.request.user.id}

    def form_valid(self, form):
        action = self.request.POST.get('action')
        if action == 'SAVE':
            return super().form_valid(form)
        elif action == 'PREVIEW':
            preview = Question(title=form.cleaned_date['title'], question=form.cleaned_data['question'])
            ctx = self.get_context_data(preview=preview)
            return self.render_to_response(ctx)
        return HttpResponseBadRequest()


class QuestionDetailView(DetailView):
    model = Question

    ACCEPT_FORM = AnswerAcceptanceForm(initial={'accepted': True})
    REJECT_FORM = AnswerAcceptanceForm(initial={'accepted': False})

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'answer_form': AnswerForm(initial={
                'user': self.request.user.id,
                'question': self.object.id,
            })
        })
        if self.object.can_accept_answers(self.request.user):
            ctx.update({
                'accept_form': self.ACCEPT_FORM,
                'reject_form': self.REJECT_FORM,
            })
        return ctx


class DailyQuestionList(DayArchiveView):
    queryset = Question.objects.all()
    date_field = 'created'
    month_format = '%m'
    allow_empty = True


class TodaysQuestionList(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        today = timezone.now()
        return reverse('quest:daily_questions', kwargs={
            'day': today.day,
            'month': today.month,
            'year': today.year
        })
