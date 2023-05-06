import pymongo
import sqlite3
import sys
import json
from pymongo import MongoClient


mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']


conn = sqlite3.connect('pokemon.sqlite')
c = conn.cursor()


c.execute('SELECT * FROM pokemon')
rows = c.fetchall()


pokemon_list = []



for row in rows:
    pokemon_dict = {
        "_id": row[0],
        "name": row[2],
        "pokedex_number": row[1],
        "types": [],
        "height": row[3],
        "weight": row[4],
        "hp": row[5],
        "attack": row[6],
        "defense": row[7],
        "speed": row[8],
        "sp_attack": row[9],
        "sp_defense": row[10],
        "abilities": []
    }
    pokemon_list.append(pokemon_dict)

# Fetch data from the database and append the types to the corresponding Pokemon dictionaries
c.execute("""
SELECT p.name AS pokemon_name, t.name AS type_name
FROM pokemon p
left JOIN pokemon_type pt ON p.id = pt.pokemon_id
left JOIN type t ON pt.type_id = t.id;
""")
results = c.fetchall()
for row in results:
    pokemon_name = row[0]
    type_name = row[1]
    for pokemon in pokemon_list:
        if pokemon['name'] == pokemon_name:
            pokemon['types'].append(type_name)

# Fetch data from the database and append the abilities to the corresponding Pokemon dictionaries
c.execute("""
SELECT p.name AS pokemon_name, a.name AS ability_name
FROM pokemon p
JOIN pokemon_abilities pa ON p.id = pa.pokemon_id
JOIN ability a ON pa.ability_id = a.id;
""")
results = c.fetchall()
for row in results:
    pokemon_name = row[0]
    ability_name = row[1]
    for pokemon in pokemon_list:
        if pokemon['name'] == pokemon_name:
            pokemon['abilities'].append(ability_name)

# Print the list of Pokemon dictionaries
for pokemon in pokemon_list:
    print(pokemon)

# Write the Pokemon data to a JSON file
with open('pokemon_data.json', 'w') as f:
    json.dump(pokemon_list, f)

# Load the data from the JSON file
with open('pokemon_data.json', 'r') as f:
    data = json.load(f)

# Insert the data into your collection
collection = pokemonDB['pokemon_data']
result = collection.insert_many(data)

# Check if the data has been successfully inserted into the collection
if result.acknowledged:
    print("Data has been successfully inserted into the collection.")
else:
    print("Data insertion failed.")
