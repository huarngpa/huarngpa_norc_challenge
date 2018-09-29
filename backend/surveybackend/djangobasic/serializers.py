from rest_framework import serializers
from djangobasic.models import Choice, Question, Response, Survey
from django.contrib.auth.models import User


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'choice_text')


class QuestionSerializer(serializers.ModelSerializer):

    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'choices',)


class SurveySerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id', 'name', 'created_at', 'questions')


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = ('id', 'user', 'question', 'choice', 'created')


class UserSerializer(serializers.ModelSerializer):

    responses = ResponseSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'responses')
