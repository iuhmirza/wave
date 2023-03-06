import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Message(models.Model):
    def __str__(self):
        return self.message_text

    def is_recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Reaction(models.Model):
    def __str__(self):
        return self.choice_text

    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
