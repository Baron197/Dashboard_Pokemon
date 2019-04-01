import plotly.graph_objs as go
import pandas as pd
import requests

res = requests.get('http://api-pokemon-baron.herokuapp.com/pokemon')
dfPokemon = pd.DataFrame(res.json(), columns=res.json()[0].keys())

listGoFunc = {
    'Bar': go.Bar,
    'Box': go.Box,
    'Violin': go.Violin
}

def generateValuePlot(legendary) :
    return {
        'x': {
            'Bar': dfPokemon[dfPokemon['Legendary'] == legendary]['Generation'].unique(),
            'Box': dfPokemon[dfPokemon['Legendary'] == legendary]['Generation'],
            'Violin': dfPokemon[dfPokemon['Legendary'] == legendary]['Generation']
        },
        'y': {
            'Bar': dfPokemon[dfPokemon['Legendary'] == legendary].groupby('Generation').mean()['Total'],
            'Box': dfPokemon[dfPokemon['Legendary'] == legendary]['Total'],
            'Violin': dfPokemon[dfPokemon['Legendary'] == legendary]['Total']
        }
    }