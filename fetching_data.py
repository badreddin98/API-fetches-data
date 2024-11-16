import requests
import json


def fetch_pokemon_data(pokemon_name):

    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon_name)
    json_data = response.text
    data = json.loads(json_data)
    
    abilities_list = []
    for ability in data['abilities']:
        abilities_list.append(ability['ability']['name'])
    
    pokemon_info = {
        'name': data['name'],
        'abilities': abilities_list,
        'weight': data['weight']
    }
    
    return pokemon_info

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight = total_weight + pokemon['weight']
    average = total_weight / len(pokemon_list)
    return average


pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = []

for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:
        pokemon_data.append(data)

if pokemon_data:
    print("\n--- Pokémon Data ---")
    for pokemon in pokemon_data:
        print("Name: " + pokemon['name'])
        print("Abilities:", pokemon['abilities'])
        print("Weight:", str(pokemon['weight']))
        print("")
    
    average_weight = calculate_average_weight(pokemon_data)
    print("Average Weight:", str(average_weight))