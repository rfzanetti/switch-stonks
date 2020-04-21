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
    title VARCHAR(100) NOT NULL,
    min_price REAL,
    min_price_country_id INTEGER,
    last_updated DATE,
    FOREIGN KEY (min_price_country_id) REFERENCES country (id)
);

CREATE TABLE listing (
    id INTEGER PRIMARY KEY,
    original_value REAL, 
    usd_value REAL, 
    date DATE,
    game_id INTEGER NOT NULL,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (game_id) REFERENCES game (id),
    FOREIGN KEY (country_id) REFERENCES country (id)
);
