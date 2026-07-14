import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publicate_date = models.DateTimeField("date published", db_column="data_publikacji")
    
    def __str__(self):
        return self.question_text
    
    @admin.display(
            boolean=True,
            ordering="publicate_date",
            description="Opublikowane niedawno?"
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publicate_date <= now

    def was_published_this_week(self):
        now = timezone.now()
        return now - datetime.timedelta(weeks=1) <= self.publicate_date <= now
    
    def in_the_future(self):
        now = timezone.now()
        return self.publicate_date >= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    