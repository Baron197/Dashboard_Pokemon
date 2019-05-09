import dash_html_components as html
import dash_core_components as dcc
from src.components.dataPokemon import dfPokemon

def renderIsiTab6() :
    return [
        html.Div([
            html.Div([
                html.P('Name : '),
                dcc.Input(
                    id='predictname',
                    type='text',
                    value='',
                    style=dict(width='100%')
                )
            ], className='col-4'),
        ], className='row')
    ]