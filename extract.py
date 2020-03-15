import json
import requests
from game import Game

ESHOP_URL = 'https://store.nintendo.com.br/'


def main():
    content = get_eshop_content(ESHOP_URL)
    game_sections = break_content_into_sections(content)

    games = [text_to_game(x) for x in game_sections]

    for game in games:
        print(game)


def get_eshop_content(url):
    return requests.get(url).text


def break_content_into_sections(content):
    games = list()

    divider = '<div class="category-product-item">'

    first_idx = content.find(divider)
    next_idx = content[first_idx + 1:].find(divider) + first_idx

    if next_idx == 0:
        games.append(content[first_idx:])
        return games

    games.append(content[first_idx:next_idx])

    games[1:1] = break_content_into_sections(content[next_idx:])

    return games


def text_to_game(raw):

    name = get_value_by_key(raw, "alt")
    price = float(get_value_by_key(raw, 'data-price-amount'))

    return Game(name, price)


def get_value_by_key(text, key):
    # TODO: Use regexp

    key_idx = text.find(key)
    end_idx = text[key_idx + len(key) + 2:].find('"') + key_idx

    return text[key_idx + len(key) + 2: end_idx + len(key) + 2]


if __name__ == '__main__':
    main()
