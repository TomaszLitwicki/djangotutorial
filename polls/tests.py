import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse

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


def create_question(quest_txt, ddd):
    time = timezone.now() + datetime.timedelta(days=ddd)
    return Question.objects.create(question_text = quest_txt, publicate_date = time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse("pollsapp:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "nie" or "Nie")
        self.assertQuerySetEqual(response.context["question_list"], [])

    def test_past_question(self):
        question = create_question("Dawne pytanie", -30)
        response = self.client.get(reverse("pollsapp:index"))
        self.assertQuerySetEqual(response.context["question_list"],[question])

    def test_future_question(self):
        create_question("Przyszłe pytanie", +30)
        response = self.client.get(reverse("pollsapp:index"))
        self.assertContains(response, "nie" or "Nie")
        self.assertQuerySetEqual(response.context["question_list"],[])

    def test_futre_and_past_question(self):
        question = create_question("przeszłe pytanie", -30) 
        create_question("przyszłe pytanie", +30)
        response = self.client.get(reverse("pollsapp:index"))
        self.assertQuerySetEqual(response.context['question_list'],[question])

    def test_two_past_question(self):
        questions = [
            create_question("Pierwsze pytanie", -10),
            create_question("Drugie pytanie", -20)
        ]
        response = self.client.get(reverse("pollsapp:index"))
        self.assertQuerySetEqual(response.context["question_list"],questions,ordered=False)


class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        future_question = create_question("Przyszłe pytanie", +5)
        url = reverse("pollsapp:ksywkadetail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question("Przeszłe pytanie", -5)
        url = reverse("pollsapp:ksywkadetail", args=(past_question.id,))
        response = self.client.get(url)
        print(f"moja wiadomość: {response.context['object']}")
        zalogowany = response.context['user']
        print(f"Użytkownik jest zalogowany - {zalogowany.is_authenticated}")
        self.assertContains(response, past_question.question_text)