from django.db import models


class User(models.Model):
    email = models.CharField(max_length=25, unique=True)
    main_currency = models.CharField(max_length=3, null=True)

    class Meta:
        db_table = 'user'
