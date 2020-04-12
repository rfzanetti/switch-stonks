import json
from tracker import ListingTracker


def main():
    with open('config.json') as json_file:
        config = json.load(json_file)
        db = config["sqlite"]["db"]

        listing_tracker = ListingTracker(db)
        listing_tracker.save_listings()


if __name__ == '__main__':
    main()
