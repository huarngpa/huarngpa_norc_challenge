from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Response
from .permissions import IsOwner, IsOwnerOrReadOnly
from .serializers import (ChoiceSerializer, QuestionSerializer,
                          ResponseSerializer,)

from rest_framework import (permissions, status, viewsets,)
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    ''' This viewset automatically provies `list` and `detail` actions. '''

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ChoiceViewSet(viewsets.ReadOnlyModelViewSet):
    ''' This viewset automatically provies `list` and `detail` actions. '''

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ResponseList(APIView):
    ''' List all snippets, or create a new snippet. '''

    @permission_classes((permissions.IsAuthenticated))
    def get(self, request, format=None):
        responses = Response.objects.all()
        serializer = ResponseSerializer(responses, many=True)
        if request.user.is_staff:
            return Response(serializer.data)
        serializer_data = [x for x in serializer.data
                           if x.user == request.user]
        return Response(serializer_data, status=status.HTTP_401_UNAUTHORIZED)

    @permission_classes((permissions.IsAuthenticated))
    def post(self, request, format=None):
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResponseViewSet(viewsets.ModelViewSet):
    ''' This viewset automatically provides `list`, `create`, `retrieve`,
        `update`, and `destroy` actions. '''

    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    permission_classes = (permissions.IsAuthenticated,)


class IndexView(generic.ListView):

    template_name = 'djangobasic/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        ''' Returns the last five published questions '''
        return Question.objects.order_by('pub_date')[:5]


class DetailView(generic.DetailView):

    model = Question
    template_name = 'djangobasic/details.html'


class ResultsView(generic.DetailView):

    model = Question
    template_name = 'djangobasic/results.html'


@login_required
def respond(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'djangobasic/details.html', {
            'question': question,
            'error_message': 'You didn\'t select a choice.',
        })
    else:
        response = Response()
        response.user = request.user
        response.question = question
        response.choice = selected_choice
        response.save()
        return HttpResponseRedirect(reverse('djangobasic:results', args=(question.id,)))
