from django.contrib import admin

from .models import Country, Currency, Coin, Issue

admin.site.register(Country)
admin.site.register(Currency)
admin.site.register(Coin)
admin.site.register(Issue)
