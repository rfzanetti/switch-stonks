CREATE TABLE country (id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, 
                      name VARCHAR(25) NOT NULL,
                      eshop_url VARCHAR(100) NOT NULL, 
                      currency_code VARCHAR(3) NOT NULL, 
                      currency_symbol VARCHAR(5), 
                      currency_usd_conversion double);
                      
CREATE TABLE game (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, 
                   name VARCHAR(100) NOT NULL);

CREATE TABLE listing (id INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT, 
                      value DOUBLE, 
                      date DATE,
                      game_id INT,
                      FOREIGN KEY (game_id) REFERENCES game(id),
                      country_id INT,
                      FOREIGN KEY (country_id) REFERENCES country(id));
