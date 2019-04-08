import pandas as pd
import requests

res = requests.get('http://api-pokemon-baron.herokuapp.com/pokemon')
dfPokemon = pd.DataFrame(res.json(), columns=res.json()[0].keys())
dfPokemonTable = pd.DataFrame(res.json(), columns=res.json()[0].keys())