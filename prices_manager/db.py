from peewee import SqliteDatabase
from model import Country, Game


class DbUtil():
    def __init__(self, db):
        self.db = SqliteDatabase(db)
        print("Connection to DB successful")

    def list_currency_codes(self):
        return [country.currency_code for country in Country.select().distinct()]

    def list_countries(self):
        return [country for country in Country.select()]

    def list_games(self):
        return [game for game in Game.select()]

    def save(self, obj):
        return obj.save()

    def update_currency_usd_conversion_rate(self, currency_code, new_rate):
        update_query = Country.update(currency_usd_conversion=new_rate).where(
            Country.currency_code == currency_code)
        update_query.execute()
