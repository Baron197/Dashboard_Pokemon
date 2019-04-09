import dash_core_components as dcc
import dash_html_components as html
from src.components.dataPokemon import dfPokemon

def renderIsiTab3() :
    return [
            html.Div([
                html.Div([
                    html.P('Hue : '),
                    dcc.Dropdown(
                        id='hueplotscatter',
                        options=[{'label': i, 'value': i} for i in ['Legendary','Generation','Type 1','Type 2']],
                        value='Legendary'
                    )
                ], className='col-4'),
                html.Div([
                    html.P('X : '),
                    dcc.Dropdown(
                        id='xplotscatter',
                        options=[{'label': i, 'value': i} for i in dfPokemon.columns[4:11]],
                        value='Attack'
                    )
                ], className='col-4'),
                html.Div([
                    html.P('Y : '),
                    dcc.Dropdown(
                        id='yplotscatter',
                        options=[{'label': i, 'value': i} for i in dfPokemon.columns[4:11]],
                        value='HP'
                    )
                ], className='col-4')
            ], className='row'),
            html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
            dcc.Graph(
                id='scattergraph'
            )
        ]