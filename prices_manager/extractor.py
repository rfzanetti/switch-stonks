import requests
from bs4 import BeautifulSoup


class ListingExtractor():

    def extract_listings(self, eshop_url):
        page = requests.get(eshop_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        game_tags = soup.find_all(class_="category-product-item")

        return [self.parse_game_tag(game_tag) for game_tag in game_tags]

    def parse_game_tag(self, game_tag):
        price = game_tag.find(class_='price-wrapper').attrs["data-price-amount"]
        title = game_tag.find(class_='category-product-item-title-link').get_text().strip()
        link = game_tag.find("a").attrs["href"]
        image_link = game_tag.find("img").attrs["src"]

        return {"game_title": title, "price": float(price), "link": link, "image_link": image_link}
