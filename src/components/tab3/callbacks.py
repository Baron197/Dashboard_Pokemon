import plotly.graph_objs as go
from src.components.dataPokemon import dfPokemon
from src.components.support import legendDict

def callbackUpdateScatterGraph(hue,x,y) :
    return dict(
                data=[
                    go.Scatter(
                        x=dfPokemon[dfPokemon[hue] == val][x],
                        y=dfPokemon[dfPokemon[hue] == val][y],
                        name=legendDict[hue][val],
                        mode='markers'
                    ) for val in dfPokemon[hue].unique()
                ],
                layout=go.Layout(
                    title= 'Scatter Plot Pokemon',
                    xaxis= { 'title': x },
                    yaxis= dict(title = y),
                    margin={ 'l': 40, 'b': 40, 't': 40, 'r': 10 },
                    hovermode='closest'
                )
            )