from prices_app.models import Game
from rest_framework import serializers


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'min_price', 'min_price_country', 'last_updated']
        depth = 1
