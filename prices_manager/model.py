from peewee import Model, SqliteDatabase, CharField, DateField, FloatField, ForeignKeyField


class BaseModel(Model):
    class Meta:
        database = SqliteDatabase("../switch_stonks.db")


class Country(BaseModel):
    name = CharField()
    eshop_url = CharField()
    currency_code = CharField()
    currency_symbol = CharField()
    currency_usd_conversion = FloatField()


class Game(BaseModel):
    title = CharField()
    min_price = FloatField()
    min_price_country_id = ForeignKeyField(Country, backref='game')
    last_updated = DateField()


class Listing(BaseModel):
    original_value = FloatField()
    usd_value = FloatField()
    date = DateField()
    game = ForeignKeyField(Game, backref='listing')
    country = ForeignKeyField(Country, backref='listing')
