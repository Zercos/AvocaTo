from django.urls import reverse
from django.utils import timezone
from django.views.generic import DayArchiveView, RedirectView

from quest.models import Question


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
