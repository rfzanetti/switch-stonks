from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.views import status
from rest_framework.test import APIRequestFactory, force_authenticate

from wishlist_app.models import Wishlist
from wishlist_app.views import WishlistDetailView
from prices_app.models import Game, Country


class ViewTests(TestCase):

    request_factory = APIRequestFactory()
    fixtures = ["user.json", "country.json", "game.json", "wishlist.json"]

    def test_delete_wishlist_game_returns_status_200(self):
        user = User.objects.get(id=1)

        request = self.request_factory.delete('/wishlist/')
        force_authenticate(request, user=user)

        response = WishlistDetailView.as_view()(request, pk=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_wishlist_entry_is_deleted_after_user_delete(self):
        user = User.objects.get(id=1)

        request = self.request_factory.delete('/wishlist/')
        force_authenticate(request, user=user)

        WishlistDetailView.as_view()(request, pk=1)

        user_wishlist = Wishlist.objects.filter(user=user)

        self.assertEqual(user_wishlist.count(), 0)

    def test_delete_wishlist_with_non_existing_game_returns_status_404(self):
        user = User.objects.get(id=1)

        request = self.request_factory.delete('/wishlist/')
        force_authenticate(request, user=user)

        response = WishlistDetailView.as_view()(request, pk=999999)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_request_with_unauthorized_user_returns_status_401(self):
        request = self.request_factory.delete('/wishlist/')
        response = WishlistDetailView.as_view()(request, pk=1)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
