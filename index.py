import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dfPokemon = pd.read_csv('PokemonKece.csv')
app = dash.Dash(__name__)

def generate_table(dataframe, max_rows=10) :
    return html.Table(
         # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(str(dataframe.iloc[i,col])) for col in range(len(dataframe.columns))
        ]) for i in range(min(len(dataframe), max_rows))]
    )

app.title = 'Dashboard Pokemon'

app.layout = html.Div([
    html.H1('Dashboard Pokemon'),
    html.H3('''
        Created By : Baron P. Hartono
    '''
    ),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Data Pokemon', value='tab-1', children=[
            html.Center([
                html.H2('Data Pokemon', className='title'),
                generate_table(dfPokemon)
            ])
        ]),
        dcc.Tab(label='Categorical Plots', value='tab-2', children=[
            dcc.Graph(
                id='example-graph',
                figure={
                    'data': [
                        {'x': ['Male','Female'], 'y': [60, 65], 'type': 'bar', 'name': 'Smoker'},
                        {'x': ['Male','Female'], 'y': [70, 75], 'type': 'bar', 'name': 'Non Smoker'},
                    ],
                    'layout': {
                        'title': 'Dash Data Visualization',
                        'xaxis': { 'title': 'Sex' },
                        'yaxis': dict(title='Avg Lifespan (Years)')
                    }
                }
            )
        ]),
    ],style={
        'fontFamily': 'system-ui'
    }, content_style={
        'fontFamily': 'Arial',
        'borderBottom': '1px solid #d6d6d6',
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'padding': '44px'
    }) 
], style={
    'maxWidth': '1200px',
    'margin': '0 auto'
})

if __name__ == '__main__':
    app.run_server(debug=True)