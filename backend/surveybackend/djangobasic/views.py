from django.contrib.auth.decorators import login_required
from django.http import (Http404, HttpResponse, HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from . import models
from .permissions import IsOwnerOrReadOnly
from .serializers import (ChoiceSerializer, QuestionSerializer,
                          ResponseSerializer,)

from rest_framework.reverse import reverse as rf_reverse
from rest_framework import (permissions, status, viewsets,)
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    ''' This viewset automatically provies `list` and `detail` actions. '''

    queryset = models.Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    ''' This viewset automatically provies `list` and `detail` actions. '''

    queryset = models.Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ResponseViewSet(viewsets.ModelViewSet):
    ''' This viewset automatically provides `list`, `create`, `retrieve`,
        `update`, and `destroy` actions. '''

    queryset = models.Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        responses = models.Response.objects.all()
        serializer = ResponseSerializer(responses, many=True)
        if request.user.is_staff:
            return Response(serializer.data)
        serializer_data = [x for x in serializer.data
                           if x['user'] == request.user.id]
        return Response(serializer_data)

    def create(self, request):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['user'] != request.user:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return models.Response.objects.get(pk=pk)
        except models.Response.DoesNotExist:
            raise Http404

    def retrieve(self, request, pk=None):
        response = self.get_object(pk)
        serializer = ResponseSerializer(response)
        if request.user.is_staff or \
                serializer.data['user'] == request.user.id:
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, pk=None):
        response = self.get_object(pk)
        serializer = ResponseSerializer(response, data=request.data)
        if serializer.is_valid():
            if request.user.is_staff or \
                    serializer.validated_data['user'] == request.user:
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        response = self.get_object(pk)
        serializer = ResponseSerializer(response, data=request.data)
        if serializer.is_valid():
            if request.user.is_staff or \
                    serializer.validated_data['user'] == request.user:
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        response = self.get_object(pk)
        if response.user == request.user:
            response.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class IndexView(generic.ListView):

    template_name = 'djangobasic/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        ''' Returns the last five published questions '''
        return models.Question.objects.order_by('pub_date')[:5]


class DetailView(generic.DetailView):

    model = models.Question
    template_name = 'djangobasic/details.html'


class ResultsView(generic.DetailView):

    model = models.Question
    template_name = 'djangobasic/results.html'


@login_required
def respond(request, question_id):
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, 'djangobasic/details.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })
    else:
        response = models.Response()
        response.user = request.user
        response.question = question
        response.choice = selected_choice
        response.save()
        return HttpResponseRedirect(reverse('djangobasic:results', args=(question.id,)))
