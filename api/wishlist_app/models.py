from django.db import models

from users_app.models import User
from prices_app.models import Game


class Wishlist(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    game = models.ForeignKey(Game, models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'wishlist'
