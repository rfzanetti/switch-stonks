from prices_app.models import Game, Listing, Country
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'last_updated']
        depth = 1


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id', 'name']


class ListingSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = Listing
        fields = ['original_value', 'usd_value', 'date', 'country']
        depth = 1


class GamePreviewSerializer(serializers.ModelSerializer):
    min_price_country = CountrySerializer()

    class Meta:
        model = Game
        fields = ['id', 'title', 'min_price', 'min_price_country', 'last_updated']
        depth = 1
