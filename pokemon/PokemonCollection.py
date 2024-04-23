import json
import requests

class PokemonCollection:
    def __init__(self):
        self.pokemon_data = {}

    def load_from_json(self, file_path):
        with open(file_path, 'r') as f:
            self.pokemon_data = json.load(f)

    def save_to_json(self, file_path):
        with open(file_path, 'w') as f:
            json.dump(self.pokemon_data, f, indent=4)

    def get_pokemon_details(self, pokemon_name):
        if pokemon_name in self.pokemon_data:
            print("Pokémon details from local database:")
            self.print_pokemon_details(self.pokemon_data[pokemon_name])
        else:
            url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
            response = requests.get(url)
            if response.status_code == 200:
                pokemon_details = response.json()
                self.pokemon_data[pokemon_name] = {
                    "name": pokemon_details["name"],
                    "type": [t["type"]["name"] for t in pokemon_details["types"]],
                    "abilities": [a["ability"]["name"] for a in pokemon_details["abilities"]],
                    "base_stats": {stat["stat"]["name"]: stat["base_stat"] for stat in pokemon_details["stats"]}
                }
                print("New Pokémon details downloaded and saved:")
                self.print_pokemon_details(self.pokemon_data[pokemon_name])
                # Save local database to JSON file
                self.save_to_json('pokemon_data.json')
            else:
                print(f"Failed to fetch details for Pokémon {pokemon_name}")

    def print_pokemon_details(self, details):
        print(f"Name: {details['name']}")
        print(f"Type: {', '.join(details['type'])}")
        print(f"Abilities: {', '.join(details['abilities'])}")
        print("Base Stats:")
        for stat, value in details['base_stats'].items():
            print(f"  {stat.capitalize()}: {value}")


