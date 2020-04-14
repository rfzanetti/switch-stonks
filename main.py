import json
from tracker import ListingTracker


def main():
    with open("config.json") as config_file:
        config = json.load(config_file)
        db_name = config['sqlite']['db']

        listing_tracker = ListingTracker(db_name)
        listing_tracker.save_listings()


if __name__ == "__main__":
    main()
