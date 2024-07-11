from django.conf import settings
from django.db import models
from django.utils import timezone

from structure.models import Address
from participant.models import Participant

VOTE_TYPE = {
    'FLOOR': 'Ответсвенный за этаж',
    'ENTRANCE': 'Ответственный за подъезд',
    'BUILDING': 'Ответсвенный за дом',
}

def vote_end():
    return timezone.now() + timezone.timedelta(days=settings.VOTE_DURATION_DAYS)

class Vote(models.Model):
    vote_type = models.CharField('Предмет голосования', max_length=20, choices=VOTE_TYPE)
    candidate = models.ForeignKey(Participant, verbose_name='Кандидат', on_delete=models.PROTECT)
    start_date = models.DateTimeField('Начало голосования', auto_now_add=True)
    vote_end = models.DateTimeField('Завершение голосования', default=vote_end)

    def __str__(self):
        return f'{self.vote_type} - {self.candidate}. {self.start_date}'
    
    class Meta:
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'
        ordering = ('-start_date', )


class VoteResults(models.Model):
    vote = models.ForeignKey(Vote, verbose_name='Голосование', on_delete=models.PROTECT)
    voice = models.ForeignKey(Participant, verbose_name='Голос', on_delete=models.PROTECT)
    choice = models.BooleanField('Выбор')
    choice_date = models.DateTimeField('Дата выбора', auto_now_add=True)

    def __str__(self):
        return f'{self.vote}. {self.choice}.  {self.choice_date}.'
    
    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'
        ordering = ('-choice_date', '-vote')


class FloorChief(models.Model):
    chief = models.ForeignKey(Participant, verbose_name='Ответсвенный за этаж', on_delete=models.PROTECT)
    start_date = models.DateTimeField('Начало срока')
    end_date = models.DateTimeField('Завершение срока', blank=True, null=True)
    address = models.ForeignKey(Address, verbose_name='Адрес', on_delete=models.PROTECT)
    entrance_number = models.PositiveSmallIntegerField('Номер подъезда')
    floor_number = models.PositiveSmallIntegerField('Номер этажа')
    active = models.BooleanField('Действующий', default=False)

    def __str__(self):
        return f'{self.chief} - {self.address}. {self.entrance_number} / {self.floor_number} c {self.start_date}'
    
    class Meta:
        verbose_name = 'Ответсвенный за этаж'
        verbose_name_plural = 'Ответсвенные по этажам'
        ordering = ('-active', 'address', 'entrance_number', 'floor_number', '-start_date')


class EntranceChief(models.Model):
    chief = models.ForeignKey(Participant, verbose_name='Ответственный за подъезд', on_delete=models.PROTECT)
    start_date = models.DateTimeField('Начало срока')
    end_date = models.DateTimeField('Завершение срока', blank=True, null=True)
    address = models.ForeignKey(Address, verbose_name='Адрес', on_delete=models.PROTECT)
    entrance_number = models.PositiveSmallIntegerField('Номер подъезда')
    active = models.BooleanField('Действующий', default=False)

    def __str__(self):
        return f'{self.chief} - {self.address}. {self.entrance_number} c {self.start_date}'
    
    class Meta:
        verbose_name = 'Ответсвенный за подъезд'
        verbose_name_plural = 'Ответсвенные по подъездам'
        ordering = ('-active', 'address', 'entrance_number', '-start_date')


class BuildingChief(models.Model):
    chief = models.ForeignKey(Participant, verbose_name='Ответственный за дом', on_delete=models.PROTECT)
    start_date = models.DateTimeField('Начало срока')
    end_date = models.DateTimeField('Завершение срока', blank=True, null=True)
    address = models.ForeignKey(Address, verbose_name='Адрес', on_delete=models.PROTECT)
    active = models.BooleanField('Действующий', default=False)

    def __str__(self):
        return f'{self.chief} - {self.address} c {self.start_date}'
    
    class Meta:
        verbose_name = 'Ответсвенный за дом'
        verbose_name_plural = 'Ответсвенные по домам'
        ordering = ('-active', 'address', '-start_date')
