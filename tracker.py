from datetime import datetime

from db import DbUtil
from extractor import ListingExtractor
from model import Game, Listing


class ListingTracker():

    def __init__(self, db):
        self.db_util = DbUtil(db)

        self.countries = self.db_util.list_countries()
        self.extractor = ListingExtractor()
        self.existing_games = self.db_util.list_games()

    def save_listings(self):
        for country in self.countries:
            self.save_country_listings(country)

    def save_country_listings(self, country):

        print(f"Extracting listings from: [{country.name}]")
        country_new_listings = self.extractor.extract_listings(country.eshop_url)

        for new_listing in country_new_listings:
            game = self.find_game_by_title(new_listing["game_title"])

            if not game:
                game = self.create_new_game(new_listing["game_title"])

            listing = Listing(listing_value=new_listing["price"],
                              listing_date=datetime.today().strftime('%Y-%m-%d'),
                              game_id=game,
                              country_id=country)

            self.db_util.store_listing(listing)

    def create_new_game(self, game_title):
        game = Game(title=game_title)

        game.id = self.db_util.store_game(game)
        self.existing_games.append(game)

        return game

    def find_game_by_title(self, game_title):
        for existing_game in self.existing_games:
            if existing_game.title == game_title:
                return existing_game

        return None
