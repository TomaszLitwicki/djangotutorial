import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

# Create your tests here.
class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(publicate_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_now_question(self):
        now_question = Question(publicate_date=timezone.now())
        self.assertIs(now_question.was_published_recently(), True)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(publicate_date = time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() + datetime.timedelta(days=1, seconds=1)
        old_quetion = Question(publicate_date = time)
        self.assertIs(old_quetion.was_published_recently(), False)

class PollsReturnsText(TestCase):
    def test_correct_returns_index_polls(self):
        response = self.client.get('/polls/')
        self.assertContains(response, 'Dzień dobry')


