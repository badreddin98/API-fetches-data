import requests
import json

def fetch_planet_data():
    response = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
    json_data = response.text
    data = json.loads(json_data)
    planets = data['bodies']
    
    planet_list = []
    
    print("\n--- Planet Data ---")
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            orbit = planet['sideralOrbit']
            
            planet_info = {
                "name": name,
                "mass": mass,
                "orbit": orbit
            }
            planet_list.append(planet_info)
            
            print("Planet:", name)
            print("Mass:", mass)
            print("Orbit Period:", orbit, "days")
            print("")
    
    return planet_list

def find_heaviest_planet(planets):
    heaviest_name = ""
    heaviest_mass = 0
    
    for planet in planets:
        if planet["mass"] > heaviest_mass:
            heaviest_mass = planet["mass"]
            heaviest_name = planet["name"]
    
    return heaviest_name, heaviest_mass


# Get all planet data
planets = fetch_planet_data()

# Find and print the heaviest planet
name, mass = find_heaviest_planet(planets)
print("The heaviest planet is", name, "with a mass of", mass, "kg")
