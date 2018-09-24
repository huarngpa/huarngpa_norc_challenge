from rest_framework import serializers
from djangobasic.models import Question, Choice, Response
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        #fields = ('url', 'id', 'question_text', 'pub_date', 'choices',)
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = '__all__'
