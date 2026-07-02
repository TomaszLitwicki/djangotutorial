from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from polls.views import index, detail, results, vote

# Create your tests here.
class HomePageAppTest(TestCase):
    def test_subpage_detail_returns_correct_info(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf-8')
        self.assertIn('Dzień dobry', html)


class PollsMappingTest(TestCase):    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/polls/')
        self.assertEqual(found.func, index)

    def test_root_url_resolves_to_details(self):
        found = resolve('/polls/1/')
        self.assertEqual(found.func, detail)

    def test_root_url_resolves_to_results(self):
        found = resolve('/polls/1/results/')
        self.assertEqual(found.func, results)

    def test_subpage_results_returns_correct_vote(self):
        found = resolve('/polls/1/vote/')
        self.assertEqual(found.func, vote)


class PollsReturnsText(TestCase):
    def test_correct_returns_index_polls(self):
        response = self.client.get('/polls/')
        self.assertContains(response, 'Dzień dobry')

    def test_correct_returns_detail_polls(self):
        response = self.client.get('/polls/1/')
        self.assertContains(response, 'question 1')

    def test_correct_returns_results_polls(self):
        response = self.client.get('/polls/1/results/')
        self.assertContains(response, 'results' and '1')

    def test_correct_returns_vote_polls(self):
        response = self.client.get('/polls/1/vote/')
        self.assertContains(response, 'voting' and '1')

