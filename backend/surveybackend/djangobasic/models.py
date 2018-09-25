import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Survey(models.Model):

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.name


class Question(models.Model):

    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=90) <= self.pub_date  <= now


class Choice(models.Model):

    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text


class Response(models.Model):

    user = models.ForeignKey(User, related_name='responses', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        str_repr = self.user.__str__() + ", "
        str_repr += self.question.__str__() + ", "
        str_repr += self.choice.__str__()
        return str_repr
