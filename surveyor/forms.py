from django import forms
from surveyor.models import Question

from .utils import RedisClient

class QuestionForm(forms.ModelForm):

    # For saving dem emails
    email = forms.EmailField()

    class Meta:
        model = Question
        fields = ['text', 'expiration']

        # Ensure that it is a date picker widget
        widget = forms.DateInput()
        widget.input_type = 'date'
        widgets = {
            'expiration': widget
        }

    def save(self, commit=True):
        """Push the new question id to redis with email, for later retrieval"""
        result = super().save(commit=commit)
        RedisClient.question_to_redis(self.cleaned_data['email'], result.id)
        return result

class AnswerForm(forms.Form):
    """Form for user to answer question"""
    answer = forms.CharField(label="Answer:", max_length=500)

    def save(self, commit=True):
        """Push the question answer to redis"""
        email = RedisClient.get_question_email(self.cleaned_data['question_id'])
        RedisClient.question_answer_to_redis(email, self.cleaned_data['question_id'],
                                             self.cleaned_data['answer'])
