from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.detail import DetailView

from surveyor.models import Question, Tag
from .forms import QuestionForm


def update_tags(request):
    """Update the tags for a question based on request"""
    pass


class NewQuestionView(CreateView):
    """Render a form to create a new question"""
    model = Question
    form_class = QuestionForm
    template_name = "question/new_question_form.html"


class QuestionView(DetailView):
    """Show either a newly created question, or expiration page"""

    model = Question
    template_name = "question.html"

    def post(self, request):
        """Handle validation and saving of user response"""
        pass

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expired'] = self.object.expiration >= timezone.now()
        return context
