from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from surveyor.models import Question, Tag
from .forms import QuestionForm


def question_view(request, question_id):
    """Show the question"""
    question = Question.objects.get(id=question_id)
    tags = Tag.objects.filter(question=question)

    data = {
        'question': question if question else None,
        'tags': tags if tags else None
    }

    return render(request, "question.html", context=data)


def update_tags(request):
    """Update the tags for a question based on request"""
    pass


def new_question(request):
    if request.method == 'POST':
        form = QuestionForm()
        if form.is_valid():
            question = Question(**form.cleaned_data)
            question.save()
            return HttpResponseRedirect('/question/{}'.format(question.id))

    elif request.method == 'GET':
        form = QuestionForm()

    data = {'form': form}
    return render(request, "question/new_question_form.html", data)
