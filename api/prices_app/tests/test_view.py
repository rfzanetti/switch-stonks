from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.views import status

from prices_app.models import Country, Game, Listing


class ViewTests(TestCase):

    client = APIClient()
    fixtures = ["country.json", "games.json", "listings.json"]

    def test_history_with_valid_id(self):
        response = self.client.get("/history/1/")

        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_history_with_invalid_id(self):
        response = self.client.get("/history/99/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_search_game_with_existing_results(self):
        response = self.client.get("/games?title=xenoblade")

        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_game_with_no_results(self):
        response = self.client.get("/games?title=mario")

        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_game_with_invalid_parameters(self):
        response = self.client.get("/games?game=stardew")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
