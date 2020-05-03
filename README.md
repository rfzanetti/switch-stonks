# Switch Stonks

This project aims to track Nintendo Switch game prices for every available country shop and make them available via REST API.


## Available Endpoints

| Endpoint                        | Method | Description                                                                |  
|---------------------------------|--------|----------------------------------------------------------------------------|
| **/games**?title={search_title} | GET    | Returns all games that contains the search parameter in its title          |
| **/history**/{game_id}/         | GET    | Returns a history of the best price for the game with the given *game_id*  |

