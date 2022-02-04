from rest_framework_json_api import serializers
from rest_framework_json_api.relations import ResourceRelatedField
from polls.models import Choice, Question, Author


class ChoiceSerializer(serializers.ModelSerializer):
    included_serializers = {
        "ask": "polls.serializers.QuestionSerializer",
    }

    class Meta:
        model = Choice
        resource_name = "Choice"
        fields = ["ask", "choice_text", "votes", "author"]

    ask = ResourceRelatedField(source='question', queryset=Question.objects, allow_null=True, required=False, default=None)
    author = ResourceRelatedField(queryset=Author.objects, allow_null=True, required=False, default=None)
