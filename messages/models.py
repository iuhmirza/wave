from django.db import models

# Create your models here.
class Message(models.Model):
    message_test = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Reactions(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
