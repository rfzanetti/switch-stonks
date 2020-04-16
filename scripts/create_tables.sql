CREATE TABLE country (
    id INTEGER PRIMARY KEY,
    name VARCHAR(25) NOT NULL,
    eshop_url VARCHAR(100) NOT NULL, 
    currency_code VARCHAR(3) NOT NULL, 
    currency_symbol VARCHAR(5), 
    currency_usd_conversion REAL
);
                      
CREATE TABLE game (
    id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL
);

CREATE TABLE listing (
    id INTEGER PRIMARY KEY,
    listing_value REAL, 
    listing_date DATE,
    game_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES game (id),
    FOREIGN KEY (country_id) REFERENCES country (id)
);
