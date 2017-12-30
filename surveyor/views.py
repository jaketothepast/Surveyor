from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView

from surveyor.models import Question, Tag
from .forms import QuestionForm, AnswerForm


def update_tags(request):
    """Update the tags for a question based on request"""
    pass


class NewQuestionView(CreateView):
    """Render a form to create a new question"""
    model = Question
    form_class = QuestionForm
    template_name = "question/new_question_form.html"

<<<<<<< HEAD
class QuestionView(FormView):
=======

class QuestionView(DetailView):
>>>>>>> master
    """Show either a newly created question, or expiration page"""

    template_name = "question.html"
    form_class = AnswerForm
    success_url = '/question/new/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        object = Question.objects.get(pk=kwargs['pk'])
        context['expired'] = self.object.expiration >= timezone.now()
        return context
