from django.contrib import admin

from .models import Address, Apartment, Building, City, District, Street

admin.site.register(Address)
admin.site.register(Apartment)
admin.site.register(Building)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Street)
