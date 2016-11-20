from django.db import models

class Event(models.Model):
    title = models.CharField('мероприятие', max_length=256)
    date = models.DateTimeField('время события')
    place = models.CharField('место проведения', max_length=256)
    description = models.TextField('описание', default='')
    image = models.ImageField('картинка', upload_to='events/', null=True, blank=True)

    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL,
                                 verbose_name='категория', blank=False, null=True)

    def __str__(self):
        return self.title
