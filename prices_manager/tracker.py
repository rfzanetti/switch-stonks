from datetime import datetime

from db import DbUtil
from extractor import ListingExtractor
from model import Game, Listing
from currency import CurrencyConverter


class ListingTracker():

    def __init__(self, db_name):
        self.db_util = DbUtil(db_name)

        self.countries = self.db_util.list_countries()
        self.extractor = ListingExtractor()
        self.existing_games = self.db_util.list_games()
        self.date = datetime.today().date()

    def save_listings(self):
        self.update_currency_values()

        for country in self.countries:
            self.save_country_listings(country)

    def update_currency_values(self):

        currency_codes = self.db_util.list_currency_codes()
        converter = CurrencyConverter()

        for code in currency_codes:
            try:
                new_usd_rate = converter.get_conversion_rate(currency_code=code, base='USD')
                self.db_util.update_currency_usd_conversion_rate(code, new_usd_rate)
            except KeyError as missing_key:
                print(f"Could not update conversion rate for currency {missing_key}")

    def save_country_listings(self, country):

        print(f"Extracting listings from: [{country.name}]")
        country_new_listings = self.extractor.extract_listings(country.eshop_url)

        for new_listing in country_new_listings:
            self.save_country_listing(new_listing, country)

    def save_country_listing(self, new_listing, country):
        game = self.find_game_by_title(new_listing["game_title"])

        new_listing_usd_value = self.calculate_usd_value(new_listing["price"], country)

        if game:
            if game.last_updated != self.date or new_listing_usd_value < game.min_price:
                self.update_game_min_price(game, new_listing_usd_value, country)
        else:
            game = self.create_new_game(new_listing, new_listing_usd_value, country)

        listing = Listing(original_value=new_listing["price"],
                          usd_value=new_listing_usd_value,
                          date=self.date,
                          game_id=game,
                          country_id=country)

        self.db_util.save(listing)

    def update_game_min_price(self, game, new_listing_usd_value, country):
        game.min_price = new_listing_usd_value
        game.min_price_country_id = country
        game.last_updated = self.date

        self.db_util.save(game)

    def calculate_usd_value(self, original_value, country):
        return original_value / country.currency_usd_conversion

    def create_new_game(self, listing, price, country):
        game = Game(title=listing["game_title"],
                    min_price=price,
                    min_price_country_id=country,
                    last_updated=self.date)

        game.id = self.db_util.save(game)
        self.existing_games.append(game)

        return game

    def find_game_by_title(self, game_title):
        for existing_game in self.existing_games:
            if existing_game.title == game_title:
                return existing_game

        return None
