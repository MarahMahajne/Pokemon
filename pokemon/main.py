from PokemonCollection import PokemonCollection
import requests
import random


def main():
    pokemon_collection = PokemonCollection()
    try:
        pokemon_collection.load_from_json('pokemon_data.json')
    except FileNotFoundError:
        pass  # File doesn't exist, start with an empty collection

    while True:
        user_input = input("Would you like to draw a Pokémon? (yes/no): ").lower()

        if user_input == 'yes':
            url = "https://pokeapi.co/api/v2/pokemon?limit=1000"
            response = requests.get(url)
            if response.status_code == 200:
                pokemon_list = response.json()['results']
                #choose a a radnom pokemon
                random_pokemon = random.choice(pokemon_list)['name']
                print(f"Random Pokémon: {random_pokemon}")
                pokemon_collection.get_pokemon_details(random_pokemon)
            else:
                print("Failed to fetch Pokémon list from API")
        elif user_input == 'no':
            print("Thank you for using the Pokémon collection program. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    pokemon_collection.save_to_json('pokemon_data.json')

if __name__ == "__main__":
    main()