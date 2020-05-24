from django.http import QueryDict
from django.db.utils import IntegrityError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from wishlist_app.models import Wishlist
from prices_app.models import Game
from prices_app.serializers import GamePreviewSerializer


class WishlistView(APIView):

    def get(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        user = request.user.id

        game_ids_in_user_wishlist = Wishlist.objects.filter(user=user).values('game')
        games = Game.objects.filter(pk__in=game_ids_in_user_wishlist)

        serializer = GamePreviewSerializer(games, many=True)

        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        user = request.user.id

        try:
            game = request.POST["game"]
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            new_wishlist_entry = Wishlist(user_id=user, game_id=game)
            new_wishlist_entry.save()
        except IntegrityError:
            return Response(f"Invalid game: {game}", status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_200_OK)


class WishlistDetailView(APIView):

    def delete(self, request, pk):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        user = request.user.id
        existing_wishlist_entry = Wishlist.objects.filter(user=user, game=pk)

        if not existing_wishlist_entry:
            return Response(status=status.HTTP_404_NOT_FOUND)

        existing_wishlist_entry.delete()

        return Response(status=status.HTTP_200_OK)
