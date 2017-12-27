from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import CreateView
from django.views.generic.detail import DetailView

from surveyor.models import Question, Tag
from .forms import QuestionForm


def question_view(request, question_id):
    """Show the question"""
    question = Question.objects.get(id=question_id)
    tags = Tag.objects.filter(question=question)

    expired = question.expired <= timezone.now()

    data = {
        'expired': expired,
        'question': question if question else None,
        'tags': tags if tags else None
    }

    return render(request, "question.html", context=data)


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expired'] = self.object.expiration >= timezone.now()
        return context