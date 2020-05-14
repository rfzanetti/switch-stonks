from rest_framework.decorators import api_view
from rest_framework.response import Response

from wishlist_app.models import Wishlist
from prices_app.models import Game
from prices_app.serializers import GamePreviewSerializer


@api_view(['POST'])
def add_game_to_user_wishlist(request):
    user = request.POST["user"]
    game = request.POST["game"]

    if not user:
        return Response(status=400)

    wishlist_entry = Wishlist(user_id=user, game_id=game)
    wishlist_entry.save()

    return Response(status=200)


@api_view(['GET'])
def list_user_wishlist_games(request):
    user = request.query_params.get('user')

    if not user:
        return Response(status=400)

    game_ids_in_user_wishlist = Wishlist.objects.filter(user=user).values('game')
    games = Game.objects.filter(pk__in=game_ids_in_user_wishlist)

    serializer = GamePreviewSerializer(games, many=True)

    return Response(serializer.data)
