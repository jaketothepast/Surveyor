from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.edit import FormView

from surveyor.models import Question
from .forms import QuestionForm, AnswerForm


class NewQuestionView(CreateView):
    """Render a form to create a new question"""
    model = Question
    form_class = QuestionForm
    template_name = "question/new_question_form.html"

class QuestionView(FormView):
    """Show either a newly created question, or expiration page"""

    template_name = "question.html"
    form_class = AnswerForm
    success_url = '/question/new/'

    def get_context_data(self, **kwargs):
        object = Question.objects.get(id=self.kwargs['pk'])
        context['object'] = object
        context['expired'] = object.expiration >= timezone.now()
        return context
