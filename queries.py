import json

# Read in the JSON file
with open('pokemon.json', 'r') as file:
    data = json.load(file)

# Example query: get all records where "type" is "water"
#pokemon = [record for record in data if record['name'] == 'Pikachu']
# pikachus = [pokemon for pokemon in data if pokemon['name'] == 'Pikachu']
# print(pikachus)
#pokemon2 = [record for record in data if record['abilties'] == 'Pikachu']
#print(pokemon)
# Example query: get the names of all grass-type Pokemon
#grass_pokemon_names = [record['name'] for record in data if 'grass' in record['typ
# es']]
#print(data)
poke =[]
for record in data:
    #print(record)

    for r in record['abilities']:
        
        if r == 'Overgrow':
            poke.append(record)
print(poke)

poke2 =[]

for record in data:
    #print(record)
     if record['name'] == 'Pikachu':
            poke2.append(record)
print(poke2)

poke3 =[]

for record in data:
    #print(record)
     if record['attack'] > 150:
            poke3.append(record)
print(poke3)
#overgrow_pokemon = [pokemon for pokemon in data['pokemon'] if 'Overgrow' in pokemon['abilities']]
  
   