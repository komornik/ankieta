import datetime
from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data publikacji', default=datetime.datetime.now())

    def __unicode__(self):
        return 'Pytanie ankiety: %s' % self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)