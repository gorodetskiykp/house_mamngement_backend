from django.db import models
from django.contrib.auth import get_user_model

from structure.models import Apartment

User = get_user_model()


class Participant(models.Model):
    auth_user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT, related_name="participants")
    apartment = models.ForeignKey(Apartment, verbose_name="Адрес", on_delete=models.PROTECT, related_name="participants")
    share = models.PositiveBigIntegerField("Доля %")
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True)
    telegram = models.CharField('Telegram', max_length=50, blank=True, null=True)
    other_contacts = models.CharField('Другие контакты', max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.apartment}'
    
    class Meta:
        verbose_name = 'Жилец'
        verbose_name_plural = 'Жильцы'
        ordering = ('apartment', )
