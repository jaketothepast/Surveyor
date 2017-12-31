from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.edit import FormView

from surveyor.models import Question
from .forms import QuestionForm, AnswerForm
from .utils import RedisClient


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
        self.object = Question.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        context['expired'] = self.object.expiration >= timezone.now()
        return context

    def form_valid(self, form):
        """With the form.cleaned_data dict, push the question answer to redis"""
        question_answer_to_redis()
