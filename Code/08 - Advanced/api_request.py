# How to connect to an API using Python

import requests  # The requests library is used to make HTTP requests in Python


base_url = "https://pokeapi.co/api/v2/"  # Base URL of the API we want to connect to


def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"  # Construct the full URL for the specific Pokémon
    response = requests.get(url)  # Make a GET request to the API and store the response in the response object
    
    if response.status_code == 200:  # Check if the request was successful
        pokemon_data = response.json()  # Parse the JSON response and store it in the variable 'pokemon_data'
        return pokemon_data
    else:
        print(f"Failed to retrieve data for {name}. Status code: {response.status_code}")  # Print an error message if the request failed


pokemon_name = "charizard"  # The name of the Pokémon we want to get information about
pokemon_info = get_pokemon(pokemon_name)  # Store the returned data in the variable 'pokemon_info'


if pokemon_info:  # Check if we received data
    print(f"Name: {pokemon_info['name'].capitalize()}")  # Print the name of the Pokémon
    print(f"Height: {pokemon_info['height']}")  # Print the height of the Pokémon
    print(f"Weight: {pokemon_info['weight']}")  # Print the weight of the Pokémon
