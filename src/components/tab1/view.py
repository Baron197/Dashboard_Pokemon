import dash_html_components as html
import dash_core_components as dcc
import dash_table as dt
from src.components.dataPokemon import dfPokemon,dfPokemonTable


# def generate_table(dataframe, max_rows=10) :
#     return html.Table(
#          # Header
#         [html.Tr([html.Th(col) for col in dataframe.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(str(dataframe.iloc[i,col])) for col in range(len(dataframe.columns))
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )

def generate_table(dataframe, pagesize=10) :
    return dt.DataTable(
                id='table-multicol-sorting',
                columns=[
                    {"name": i, "id": i} for i in dataframe.columns
                ],
                pagination_settings={
                    'current_page': 0,
                    'page_size': pagesize
                },
                pagination_mode='be',
                style_table={'overflowX': 'scroll'},
                sorting='be',
                sorting_type='multi',
                sorting_settings=[]
            )
            
def renderIsiTab1() :
    return [
            html.Div([
                html.Div([
                    html.P('Name : '),
                    dcc.Input(
                        id='filternametable',
                        type='text',
                        value='',
                        style=dict(width='100%')
                    )
                ], className='col-4'),
                html.Div([
                    html.P('Generation : '),
                    dcc.Dropdown(
                        id='filtergenerationtable',
                        options=[i for i in [{ 'label': 'All Generation', 'value': '' },
                                            { 'label': '1st Generation', 'value': '1' },
                                            { 'label': '2nd Generation', 'value': '2' },
                                            { 'label': '3rd Generation', 'value': '3' },
                                            { 'label': '4th Generation', 'value': '4' },
                                            { 'label': '5th Generation', 'value': '5' },
                                            { 'label': '6th Generation', 'value': '6' }]],
                        value=''
                    )
                ], className='col-4'),
                html.Div([
                    html.P('Category : '),
                    dcc.Dropdown(
                        id='filtercategorytable',
                        options=[i for i in [{ 'label': 'All Category', 'value': '' },
                                            { 'label': 'Legendary', 'value': 'True' },
                                            { 'label': 'Non-Legendary', 'value': 'False' }]],
                        value=''
                    )
                ], className='col-4')
            ], className='row'),
            html.Br(),
            html.Div([
                html.Div([
                    html.P('Total : '),
                    dcc.RangeSlider(
                        marks={i: str(i) for i in range(dfPokemon['Total'].min(), dfPokemon['Total'].max()+1,100)},
                        min=dfPokemon['Total'].min(),
                        max=dfPokemon['Total'].max(),
                        value=[dfPokemon['Total'].min(),dfPokemon['Total'].max()],
                        className='rangeslider',
                        id='filtertotaltable'
                    )
                ], className='col-9'),
                html.Div([

                ],className='col-1'),
                html.Div([
                    html.Br(),
                    html.Button('Search', id='buttonsearch', style=dict(width='100%'))
                ], className='col-2')
            ], className='row'),
            html.Br(),html.Br(),html.Br(),
            html.Div([
                html.Div([
                    html.P('Max Rows : '),
                    dcc.Input(
                        id='filterrowstable',
                        type='number',
                        value=10,
                        style=dict(width='100%')
                    )
                ], className='col-1')
            ], className='row'),
            html.Center([
                html.H2('Data Pokemon', className='title'),
                html.Div(id='tablediv', children=generate_table(dfPokemonTable))
            ])
        ]