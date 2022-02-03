from rest_framework_json_api import serializers
from polls.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        resource_name = "Question"
        fields = ["question_text", "pub_date"]