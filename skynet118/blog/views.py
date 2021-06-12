from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Question, Choice
#from django.template import loader

from django.urls import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.

#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    context = {
#            'latest_question_list': latest_question_list,
#            }
#
#    return render(request, 'blog/index.html', context) 
#
#def vote(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        return render(request, 'blog/detail.html', {'question': question, 'error_message': "You didn't select a choice",})
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))
#
#def detail(request, question_id):
#    try:
#        question = get_object_or_404(Question, pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#
#    return render(request, 'blog/detail.html', {'question': question})
#
#
#def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'blog/results.html', {'question': question})

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'blog/detail.html', {'question': question, 'error_message': "You didn't select a choice",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('blog:results', args=(question.id,)))















