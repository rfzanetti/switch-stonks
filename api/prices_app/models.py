from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=25)
    eshop_url = models.CharField(max_length=100)
    currency_code = models.CharField(max_length=3)
    currency_symbol = models.CharField(max_length=5, blank=True, null=True)
    currency_usd_conversion = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'country'


class Game(models.Model):
    title = models.CharField(max_length=80)
    min_price = models.FloatField(blank=True, null=True)
    min_price_country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'game'


class Listing(models.Model):
    original_value = models.FloatField(blank=True, null=True)
    usd_value = models.FloatField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    country = models.ForeignKey(Country, models.DO_NOTHING)

    class Meta:
        db_table = 'listing'
