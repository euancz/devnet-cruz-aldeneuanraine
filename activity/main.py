import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
response2 = requests.get("https://pokeapi.co/api/v2/pokemon/49")
response3 = requests.get("https://pokeapi.co/api/v2/pokemon/70")
response4 = requests.get("https://pokeapi.co/api/v2/pokemon/32")
response5 = requests.get("https://pokeapi.co/api/v2/pokemon/111")

pokemon = response.json()
name = pokemon.get("name")
height = pokemon.get("height")
weight = pokemon.get("weight")

print(f"{height}, {weight}")

pokemon2 = response2.json()
name2 = pokemon2.get("name")
height2 = pokemon2.get("height")
weight2 = pokemon2.get("weight")

print(f"{height2}, {weight2}")

pokemon3 = response3.json()
name3 = pokemon3.get("name")
height3 = pokemon3.get("height")
weight3 = pokemon3.get("weight")

print(f"{height3}, {weight3}")

pokemon4 = response4.json()
name4 = pokemon4.get("name")
height4 = pokemon4.get("height")
weight4 = pokemon4.get("weight")

print(f"{height4}, {weight4}")

pokemon5 = response5.json()
name5 = pokemon5.get("name")
height5 = pokemon5.get("height")
weight5 = pokemon5.get("weight")

print(f"{height5}, {weight5}")



