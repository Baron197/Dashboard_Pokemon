import plotly.graph_objs as go
from src.components.dataPokemon import dfPokemon

listGoFunc = {
    'Bar': go.Bar,
    'Box': go.Box,
    'Violin': go.Violin
}

def generateValuePlot(legendary, x, y, stats = 'mean') :
    return {
        'x': {
            'Bar': dfPokemon[dfPokemon['Legendary'] == legendary][x].unique(),
            'Box': dfPokemon[dfPokemon['Legendary'] == legendary][x],
            'Violin': dfPokemon[dfPokemon['Legendary'] == legendary][x]
        },
        'y': {
            'Bar': dfPokemon[dfPokemon['Legendary'] == legendary].groupby(x)[y].describe()[stats],
            'Box': dfPokemon[dfPokemon['Legendary'] == legendary][y],
            'Violin': dfPokemon[dfPokemon['Legendary'] == legendary][y]
        }
    }