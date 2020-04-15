from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from prices_app.models import Country, Game, Listing
from prices_app.serializers import CountrySerializer, GameSerializer, ListingSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().order_by('name')
    serializer_class = CountrySerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['name']


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('title')
    serializer_class = GameSerializer

    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['title']


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
