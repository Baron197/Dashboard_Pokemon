import dash_core_components as dcc
import dash_html_components as html
from src.components.dataPokemon import dfPokemon

def renderIsiTab2() :
    return [
            html.Div([
                html.Div([
                    html.P('Jenis : '),
                    dcc.Dropdown(
                        id='jenisplotcategory',
                        options=[{'label': i, 'value': i} for i in ['Bar','Box','Violin']],
                        value='Bar'
                    )
                ], className='col-3'),
                html.Div([
                    html.P('X : '),
                    dcc.Dropdown(
                        id='xplotcategory',
                        options=[{'label': i, 'value': i} for i in ['Generation','Type 1','Type 2']],
                        value='Generation'
                    )
                ], className='col-3'),
                html.Div([
                    html.P('Y : '),
                    dcc.Dropdown(
                        id='yplotcategory',
                        options=[{'label': i, 'value': i} for i in dfPokemon.columns[4:11]],
                        value='Total'
                    )
                ], className='col-3'),
                html.Div([
                    html.P('Stats : '),
                    dcc.Dropdown(
                        id='statsplotcategory',
                        options=[i for i in [{ 'label': 'Mean', 'value': 'mean' },
                                            { 'label': 'Standard Deviation', 'value': 'std' },
                                            { 'label': 'Count', 'value': 'count' },
                                            { 'label': 'Min', 'value': 'min' },
                                            { 'label': 'Max', 'value': 'max' },
                                            { 'label': '25th Percentiles', 'value': '25%' },
                                            { 'label': 'Median', 'value': '50%' },
                                            { 'label': '75th Percentiles', 'value': '75%' }]],
                        value='mean',
                        disabled=False
                    )
                ], className='col-3')
            ], className='row'),
            html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
            dcc.Graph(
                id='categorygraph'
            )
        ]