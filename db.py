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

    def store_game(self, game):
        return game.save()

    def store_listing(self, listing):
        listing.save()

    def update_currency(self, currency_code, new_rate):
        countries_with_currency = Country.select().where(Country.currency_code == currency_code)

        for country in countries_with_currency:
            country.currency_usd_conversion = new_rate
            country.save()
