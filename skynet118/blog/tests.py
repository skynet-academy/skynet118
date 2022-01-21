from django.test import TestCase

# Create your tests here.

import datetime 

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):

    def test_published_recently(self):
        """ 
            was published recently returns False for questions whose pub_date in the 
            future 
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), False)

    def test_published_recently_with_recent_question(self):
        """
            published_recently returns True for questions whose pub_date is within the last day
        """

        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.published_recently(), True)


    def create_question(question_text, days):
        """
            Create a question with the given 'question_text'
            and published the given number of 'days' offset to now (negative for questions published)
            in the past, positive for question that have 

        """
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text, pub_date=time)



class QuestionIndexViewTest(TestCase):
    def test_no_question(self):
        """ 
            if no question exist, an appropriate message is displayed
        """

        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No blog are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
            Question with a pub_date in the past are displayed on the index page
        """
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question],)
        

    def test_future_question(self):
        """
            Questions with a pub_date in the future aren't displayed on the index page.
        """
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, "No blog are available")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_future_question_and_past_question(self):
        """
            Even if both past and future questions exist, only past questions are displayed
        """
        question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('blog:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question],)

    def test_two_past_questions(self):
        """
            The questions index page my display multiple questions
        """
        question1 = create_question(question_text="Past question1.", days=30)
        question2 = create_question(question_text="Past question2.", days=-5)
        response = self.client.get(reverse("blog:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [question2, question1],)


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
            The detail view of a question with a pub_date in the future
            returns a 404 not found.
        """
        future_question = create_question(question_text="Future question", days=5)
        url = reverse("blog:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
            The detail view of a question with a pub_date in the past displays the question's text 
        """
        past_question = create_question(question_text="Past Question", days=-5)
        url = reverse("blog:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

