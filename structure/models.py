# pylint: disable=C0114,R0903,E0307,C0116,C0115

from django.db import models


class City(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name', )


class District(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ('name', )


class Street(models.Model):
    name = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'
        ordering = ('name', )


class Address(models.Model):
    city = models.ForeignKey(City, verbose_name='Город', on_delete=models.PROTECT, related_name='city_addresses')
    district = models.ForeignKey(District, verbose_name='Район', on_delete=models.PROTECT, related_name='disctict_addresses')
    street = models.ForeignKey(Street, verbose_name='Улица', on_delete=models.PROTECT, related_name='street_addresses')
    building_number = models.CharField('Номер дома', max_length=100)

    def __str__(self):
        return f'{self.street} {self.building_number}. {self.city}, {self.district}'
    
    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'
        ordering = ('city', 'district', 'street', 'building_number')


class Building(models.Model):
    address = models.OneToOneField(Address, verbose_name='Адрес', on_delete=models.PROTECT, related_name='buildings')
    entrance_count = models.PositiveSmallIntegerField('Количество подъездов')
    floor_count = models.PositiveSmallIntegerField('Количество этажей')

    def __str__(self):
        return str(self.address)
    
    class Meta:
        verbose_name = 'Здание'
        verbose_name_plural = 'Здания'
        ordering = ('address', )


class Apartment(models.Model):
    address = models.ForeignKey(Address, verbose_name='Адрес', on_delete=models.PROTECT, related_name='apartments')
    apartment_number = models.PositiveSmallIntegerField('Номер квартиры')
    entrance_number = models.PositiveSmallIntegerField('Номер подъезда')
    floor_number = models.PositiveSmallIntegerField('Номер этажа')
    
    def __str__(self):
        return f'{self.apartment_number} [{self.entrance_number}, {self.floor_number}], {self.address}'
    
    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'
        ordering = ('address', 'apartment_number')

    def get_apartments(self, address, entrance_number=None, floor_number=None):
        return Apartment.objects.filter(**{field: arg for field, arg in {
            'address':address, 'entrance_number':entrance_number, 'floor_number':floor_number} if arg})
