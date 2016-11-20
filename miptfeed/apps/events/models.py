from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=256)
    date = models.DateTimeField('время события')
    place = models.CharField(max_length=256)
    description = models.TextField('описание события', default='')

    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL,
                                 blank=False, null=True)

    def __str__(self):
        return self.title
