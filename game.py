import json


class Game():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return json.dumps(self, default=lambda x: vars(x), ensure_ascii=False)
