from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.views import status
from rest_framework.test import APIRequestFactory, force_authenticate

from wishlist_app.models import Wishlist
from wishlist_app.views import WishlistView
from prices_app.models import Game, Country
from prices_app.serializers import GamePreviewSerializer


class ViewTests(TestCase):

    request_factory = APIRequestFactory()

    @staticmethod
    def create_game(id, title, min_price, min_price_country, last_updated):
        return Game.objects.create(id=id,
                                   title=title,
                                   min_price=min_price,
                                   min_price_country=min_price_country,
                                   last_updated=last_updated)

    def setUp(self):
        User.objects.create_user('some_user', 'some_password')

        brazil = Country.objects.create(id=1,
                                        name="Brazil",
                                        eshop_url="https://store.nintendo.com.br/",
                                        currency_code="BRL",
                                        currency_symbol="R$",
                                        currency_usd_conversion=4.25)

        self.create_game(1, "Yooka-Laylee", 8.89, brazil, "2020-05-03")
        self.create_game(2, "Stardew Valley", 2.43, brazil, "2020-05-03")

    def test_get_user_wishlist_returns_status_200(self):
        user = User.objects.get(id=1)

        request = self.request_factory.get('/wishlist/')
        force_authenticate(request, user=user)
        response = WishlistView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_wishlist_returns_empty_list_when_it_is_empty(self):
        user = User.objects.get(id=1)

        request = self.request_factory.get('/wishlist/')
        force_authenticate(request, user=user)
        response = WishlistView.as_view()(request)

        self.assertEqual(response.data, [])

    def test_get_user_wishlist_returns_expected_game(self):
        user = User.objects.get(id=1)
        game = Game.objects.get(id=1)

        Wishlist.save(Wishlist(user=user, game=game))

        request = self.request_factory.get('/wishlist/')
        force_authenticate(request, user=user)

        response = WishlistView.as_view()(request)
        expected_game = GamePreviewSerializer(game)

        self.assertEqual(response.data[0], expected_game.data)

    def test_get_user_wishlist_returns_multiple_expected_games(self):
        user = User.objects.get(id=1)
        games = Game.objects.all()

        for game in games:
            Wishlist.save(Wishlist(user=user, game=game))

        request = self.request_factory.get('/wishlist/')
        force_authenticate(request, user=user)

        response = WishlistView.as_view()(request)
        expected_game = GamePreviewSerializer(games, many=True)

        self.assertEqual(response.data, expected_game.data)

    def test_post_game_in_user_wishlist_returns_status_200(self):
        user = User.objects.get(id=1)
        request = self.request_factory.post('/wishlist/', {"game": 1})
        force_authenticate(request, user=user)

        response = WishlistView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wishlist_entry_is_saved_after_user_post(self):
        user = User.objects.get(id=1)
        request = self.request_factory.post('/wishlist/', {"game": 1})
        force_authenticate(request, user=user)

        WishlistView.as_view()(request)

    def test_post_wishlist_with_non_existing_game_returns_status_404(self):
        user = User.objects.get(id=1)
        request = self.request_factory.post('/wishlist/', {"game": 9999})
        force_authenticate(request, user=user)

        response = WishlistView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_post_wishlist_without_game_parameter_returns_status_400(self):
        user = User.objects.get(id=1)
        request = self.request_factory.post('/wishlist/', {"not_game": 1})
        force_authenticate(request, user=user)

        response = WishlistView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_request_with_unauthorized_user_returns_status_401(self):
        request = self.request_factory.get('/wishlist/')
        response = WishlistView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_request_with_unauthorized_user_returns_status_401(self):
        request = self.request_factory.post('/wishlist/', {})
        response = WishlistView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
