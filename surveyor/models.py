from django.db import models
from django.utils import timezone

class Tag(models.Model):
    question = models.ForeignKey("Question", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

class Question(models.Model):
    text = models.CharField(max_length=200)
    expiration = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return f"/question/{self.id}"

class Answer(models.Model):
    question = models.ForeignKey("Question")
    text = models.CharField(max_length=500)
