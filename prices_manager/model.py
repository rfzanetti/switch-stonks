from peewee import Model, SqliteDatabase, CharField, DateField, FloatField, ForeignKeyField

db = SqliteDatabase("../switch_stonks.db")


class Country(Model):
    name = CharField()
    eshop_url = CharField()
    currency_code = CharField()
    currency_symbol = CharField()
    currency_usd_conversion = FloatField()

    class Meta:
        database = db


class Game(Model):
    title = CharField()
    min_price = FloatField()
    min_price_country_id = ForeignKeyField(Country, backref='game')
    last_updated = DateField()

    class Meta:
        database = db


class Listing(Model):
    original_value = FloatField()
    usd_value = FloatField()
    date = DateField()
    game = ForeignKeyField(Game, backref='listing')
    country = ForeignKeyField(Country, backref='listing')

    class Meta:
        database = db
