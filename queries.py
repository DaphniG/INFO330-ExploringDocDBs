import json

# Read in the JSON file
with open('pokemon.json', 'r') as file:
    data = json.load(file)

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
  
   
