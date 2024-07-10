from django.db import models

from participant.models import Participant


class ServiceRequest(models.Model):
    register_date = models.DateTimeField('Дата регистрации заявки', auto_now_add=True)
    author = models.ForeignKey(Participant, verbose_name='Автор заявки', on_delete=models.PROTECT)
    text = models.TextField('Заявка')

    def __str__(self):
        return f'{self.number} от {self.register_date}'
    
    @property
    def number(self):
        return f'SR-{self.pk}'
    
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('-register_date', )