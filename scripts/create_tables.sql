CREATE TABLE currency (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
                       code VARCHAR(3) NOT NULL, 
                       symbol VARCHAR(5), 
                       usd_conversion double);

CREATE TABLE country (id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, 
                      name VARCHAR(25) NOT NULL,
                      eshop_url VARCHAR(100) NOT NULL, 
                      currency_id INT,
                      FOREIGN KEY (currency_id) REFERENCES currency(id));
                      
CREATE TABLE game (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
                   name VARCHAR(100) NOT NULL);

CREATE TABLE price (id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, 
                    value DOUBLE, 
                    timestamp BIGINT,
                    game_id INT,
                    FOREIGN KEY (game_id) REFERENCES game(id),
                    country_id INT,
                    FOREIGN KEY (country_id) REFERENCES country(id));