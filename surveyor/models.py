from django.db import models

class Tag(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Question(models.Model):
    text = models.CharField(max_length=200)
