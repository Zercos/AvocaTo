from django.conf import settings
from django.db import models
from django.urls.base import reverse


class Question(models.Model):
    NEW = 1
    ON_REVIEW = 2
    ACCEPTED = 3
    POSTED = 4
    DELETED = 5
    STATUSES = (
        (NEW, 'New'), (ON_REVIEW, 'On review'), (ACCEPTED, 'Accepted'), (DELETED, 'Deleted')
    )

    title = models.CharField(max_length=130, null=False, blank=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.TextField(null=False, blank=False)
    created = models.DateField(auto_now_add=True, null=False)
    updated = models.DateField(auto_now=True)
    status = models.IntegerField(choices=STATUSES, default=NEW)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('quest:question_detail', kwargs={'pk': self.id})

    def can_accept_answers(self, user):
        return user == self.user


class Answer(models.Model):
    answer = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, null=False)
    updated = models.DateField(auto_now=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
