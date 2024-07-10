from django.db import models
from django.contrib.auth import get_user_model

from structure.models import Apartment

User = get_user_model()


class Participant(models.Model):
    auth_user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.PROTECT, related_name="participants")
    apartment = models.ForeignKey(Apartment, verbose_name="Адрес", on_delete=models.PROTECT, related_name="participants")
    share = models.PositiveBigIntegerField("Доля %")
    is_floor_chief = models.BooleanField("Главный по этажу", default=False)
    is_entrance_chief = models.BooleanField("Главный по подъезду", default=False)
    is_building_chief = models.BooleanField("Главный по дому", default=False)

    def __str__(self):
        return f'{self.apartment}'
    
    class Meta:
        verbose_name = 'Жилец'
        verbose_name_plural = 'Жильцы'
        ordering = ('apartment', )
