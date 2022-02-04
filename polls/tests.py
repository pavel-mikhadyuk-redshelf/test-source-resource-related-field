from django.test import TestCase
from .serializers import ChoiceSerializer
from .models import Question, Author
from django.utils import timezone


class QuestionSerializerTestCase(TestCase):
    def test_question_serializer(self):
        self.maxDiff = None
        question = Question.objects.create(question_text='text', pub_date=timezone.now())
        author = Author.objects.create(first_name='Joan', last_name='Rolling')
        choice_text, votes = 'something', 2
        data = {
            'choice_text': choice_text,
            'votes': votes,
            'ask': {
                'id': question.id,
                'type': 'Question',
            }
        }
        serializer = ChoiceSerializer(data=data)
        is_valid = serializer.is_valid(raise_exception=True)
        self.assertTrue(is_valid)
        choice = serializer.save()
        self.assertEqual(choice.votes, votes)
        self.assertEqual(choice.choice_text, choice_text)
        self.assertEqual(choice.question, question)
