from django import forms


class QuestionForm(forms.Form):
    text = forms.CharField(label='Question', max_length=200)
