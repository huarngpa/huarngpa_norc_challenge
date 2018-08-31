from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Response

# Create your views here.


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
