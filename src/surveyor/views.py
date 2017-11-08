from django.shortcuts import render

from surveyor.models import Question, Tag

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
