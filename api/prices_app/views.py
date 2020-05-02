from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from prices_app.models import Game, Listing
from prices_app.serializers import GamePreviewSerializer, ListingSerializer


@api_view(['GET'])
def list_game_by_title(request):
    title = request.query_params.get('title')

    if not title:
        return Response(status=400)

    games = Game.objects.filter(title__contains=title)
    serializer = GamePreviewSerializer(games, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def game_listing_history(request, pk):
    query = f"""SELECT id, original_value, MIN(usd_value), date, game_id, country_id
                FROM listing
                WHERE game_id = {pk}
                GROUP BY date"""

    listings = Listing.objects.raw(query)

    if listings:
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)
    else:
        raise NotFound(code=404)
