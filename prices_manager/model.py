from peewee import Model, SqliteDatabase, CharField, DateField, FloatField, ForeignKeyField

db = SqliteDatabase("../switch_stonks.db")


class Game(Model):
    title = CharField()

    class Meta:
        database = db


class Country(Model):
    name = CharField()
    eshop_url = CharField()
    currency_code = CharField()
    currency_symbol = CharField()
    currency_usd_conversion = FloatField()

    class Meta:
        database = db


class Listing(Model):
    listing_value = FloatField()
    listing_date = DateField()
    game = ForeignKeyField(Game, backref='listing')
    country = ForeignKeyField(Country, backref='listing')

    class Meta:
        database = db
