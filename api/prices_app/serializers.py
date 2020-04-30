from prices_app.models import Game, Listing
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'min_price', 'min_price_country', 'last_updated']
        depth = 1


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['original_value', 'usd_value', 'date', 'game', 'country']
        depth = 1
