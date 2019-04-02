import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from categoryPlot import dfPokemon, listGoFunc, generateValuePlot, go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
            html.Div([
                html.Div([
                    html.P('Jenis : '),
                    dcc.Dropdown(
                        id='jenisplotcategory',
                        options=[{'label': i, 'value': i} for i in ['Bar','Box','Violin']],
                        value='Bar'
                    )
                ], className='col-4'),
                html.Div([
                    html.P('X : '),
                    dcc.Dropdown(
                        id='xplotcategory',
                        options=[{'label': i, 'value': i} for i in ['Generation','Type 1','Type 2']],
                        value='Generation'
                    )
                ], className='col-4'),
                html.Div([
                    html.P('Y : '),
                    dcc.Dropdown(
                        id='yplotcategory',
                        options=[{'label': i, 'value': i} for i in dfPokemon.columns[4:11]],
                        value='Total'
                    )
                ], className='col-4')
            ], className='row'),
            html.Br(),
            dcc.Graph(
                id='categorygraph'
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

@app.callback(
    Output(component_id='categorygraph', component_property='figure'),
    [Input(component_id='jenisplotcategory', component_property='value'),
    Input(component_id='xplotcategory', component_property='value'),
    Input(component_id='yplotcategory', component_property='value')]
)
def update_category_graph(jenisplot,x,y):
    return dict(
        layout= go.Layout(
            title= '{} Plot Pokemon'.format(jenisplot),
            xaxis= { 'title': x },
            yaxis= dict(title=y),
            boxmode='group',
            violinmode='group'
        ),
        data=[
            listGoFunc[jenisplot](
                x=generateValuePlot('True',x,y)['x'][jenisplot],
                y=generateValuePlot('True',x,y)['y'][jenisplot],
                name='Legendary'
            ),
            listGoFunc[jenisplot](
                x=generateValuePlot('False',x,y)['x'][jenisplot],
                y=generateValuePlot('False',x,y)['y'][jenisplot],
                name='Non-Legendary'
            )
        ]
    )

if __name__ == '__main__':
    app.run_server(debug=True)