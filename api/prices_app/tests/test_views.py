from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.views import status

from prices_app.models import Country, Game, Listing


class ViewTests(TestCase):

    client = APIClient()

    @staticmethod
    def create_listing(id, original_value, usd_value, date, game, country):
        return Listing.objects.create(id=id,
                                      original_value=original_value,
                                      usd_value=usd_value,
                                      date=date,
                                      game=game,
                                      country=country)

    @staticmethod
    def create_game(id, title, min_price, min_price_country, last_updated):
        return Game.objects.create(id=id,
                                   title=title,
                                   min_price=min_price,
                                   min_price_country=min_price_country,
                                   last_updated=last_updated)

    def setUp(self):
        brazil = Country.objects.create(id=1,
                                        name="Brazil",
                                        eshop_url="https://store.nintendo.com.br/",
                                        currency_code="BRL",
                                        currency_symbol="R$",
                                        currency_usd_conversion=4.25)

        yooka_laylee = self.create_game(1, "Yooka-Laylee", 8.89, brazil, "2020-05-03")
        stardew_valley = self.create_game(2, "Stardew Valley", 2.43, brazil, "2020-05-03")

        self.create_listing(1, 40, 8.89, "2020-05-03", yooka_laylee, brazil)
        self.create_listing(2, 38.90, 8.75, "2020-05-02", yooka_laylee, brazil)
        self.create_listing(3, 11.50, 2.43, "2020-05-03", stardew_valley, brazil)
        self.create_listing(4, 11.40, 2.41, "2020-05-02", stardew_valley, brazil)

    def test_history_with_valid_id(self):
        response = self.client.get("/history/1/")

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_history_with_invalid_id(self):
        response = self.client.get("/history/99/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_game_with_existing_results(self):
        response = self.client.get("/games?title=yooka")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_game_with_no_results(self):
        response = self.client.get("/games?title=mario")

        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_game_with_invalid_parameters(self):
        response = self.client.get("/games?game=stardew")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
