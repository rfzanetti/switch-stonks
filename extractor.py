import requests


class ListingExtractor():

    def extract_listings(self, eshop_url):
        eshop_content = requests.get(eshop_url).text
        listing_sections = self.break_content_into_sections(eshop_content)

        return [self.extract_listing_from_section(section) for section in listing_sections]

    def extract_listing_from_section(self, section):
        game = self.get_value_by_key(section, "alt")
        price = float(self.get_value_by_key(section, 'data-price-amount'))

        return {"game_title": game, "price": price}

    def break_content_into_sections(self, content):
        sections = list()

        divider = '<div class="category-product-item">'

        first_idx = content.find(divider)
        next_idx = content[first_idx + 1:].find(divider) + first_idx

        if next_idx == 0:
            sections.append(content[first_idx:])
            return sections

        sections.append(content[first_idx:next_idx])

        sections[1:1] = self.break_content_into_sections(content[next_idx:])

        return sections

    def get_value_by_key(self, text, key):
        # TODO: Use regexp

        key_idx = text.find(key)
        end_idx = text[key_idx + len(key) + 2:].find('"') + key_idx

        return text[key_idx + len(key) + 2: end_idx + len(key) + 2]
