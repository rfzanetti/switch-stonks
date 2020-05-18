from django.db.utils import IntegrityError

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from wishlist_app.models import Wishlist
from prices_app.models import Game
from prices_app.serializers import GamePreviewSerializer


@api_view(['POST'])
def add_game_to_user_wishlist(request):
    if not request.user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    user = request.user.id
    game = request.POST["game"]

    try:
        new_wishlist_entry = Wishlist(user_id=user, game_id=game)
        new_wishlist_entry.save()
    except IntegrityError:
        return Response(f"Invalid game: {game}", status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def list_user_wishlist_games(request):
    if not request.user.is_authenticated:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    user = request.user.id

    game_ids_in_user_wishlist = Wishlist.objects.filter(user=user).values('game')
    games = Game.objects.filter(pk__in=game_ids_in_user_wishlist)

    serializer = GamePreviewSerializer(games, many=True)

    return Response(serializer.data)
