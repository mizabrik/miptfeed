from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField('время события')
    place = models.CharField(max_length=256)
    description = models.TextField('описание события', default='')
