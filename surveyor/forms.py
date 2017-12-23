from django import forms
from surveyor.models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['text', 'expiration']

        # Ensure that it is a date picker widget
        widget = forms.DateInput()
        widget.input_type = 'date'
        widgets = {
            'expiration': widget
        }
