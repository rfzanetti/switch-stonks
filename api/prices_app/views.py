from rest_framework import viewsets, filters

from prices_app.models import Game
from prices_app.serializers import GameSerializer


class GameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Game.objects.all().order_by('title')
    serializer_class = GameSerializer

    filter_backends = [filters.SearchFilter]
    filter_fields = ['title']
