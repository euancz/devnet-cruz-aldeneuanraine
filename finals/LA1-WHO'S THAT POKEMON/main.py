import requests
import random 

def get_pokemon():
    pokemons = []
    used_id = []
    while len(pokemons) < 5:
        pokemonid = random.randint(1, 1351)
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemonid}")
        if response.status_code == 200:
            if pokemonid not in used_id:
                pokemons.append(response)
                used_id.append(pokemonid)
    return pokemons

def poke_data():
    pokemons = get_pokemon()
    pokedata = random.choice(pokemons).json()
    name = pokedata['name']
    height = pokedata['height']
    weight = pokedata['weight']
    ability = pokedata['abilities'][0]['ability']['name']
    poketype = pokedata['types'][0]['type']['name']
    return name, height, weight, ability, poketype, pokemons

def user_guess():
    print("------------------------")
    userinp = input("Enter your guess: ")
    return userinp.lower()

def main():
    name, height, weight, ability, poketype, pokemons = poke_data()
    Tries = 3
    Running = True
    print("------------------------")
    print(f"Who's that Pokemon? \nHeight: {height}  \nWeight: {weight} \nAbility: {ability} \nType: {poketype}.")
    print("------------------------")
    print("Here are your choices:")
    for pokemon in pokemons:
        print(f"{pokemon.json()['name']}")
    while Running:
        print("------------------------")
        print("Can you guess which one it is?")
        userinp = user_guess()
        if userinp == name:
            print("------------------------")
            print("Correct!")
            Running = False
        elif userinp == "exit":
            Running = False
            print("------------------------")
            print("Thanks for playing!")
        else:
            Tries -= 1
            if Tries > 0:
                print("------------------------")
                print(f"Wrong! Try again.")
            elif Tries <= 0:
                print("------------------------")
                print(f"You've used all your tries! The correct answer was {name}.")
                Running = False
main()
