import base64
import datetime
import io
import pandas as pd
import dash_table

import pickle
import requests
import dash_html_components as html
loadModel = pickle.load(open('rfc_pokemon.sav', 'rb'))
encoderType1 = pickle.load(open('le_type1.sav', 'rb'))
encoderType2 = pickle.load(open('le_type2.sav', 'rb'))

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = pd.read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file.'
        ])
    
    df['Type 1'] = encoderType1.transform(df['Type 1'])
    df['Type 2'] = encoderType2.transform(df['Type 2'])
    predictProba = loadModel.predict_proba(df.drop(['#','Legendary','Name'], axis=1))

    predictions = []
    for prob in predictProba[:,1] :
        if(prob > 0.15) :
            predictions.append('Legendary')
        else :
            predictions.append('Normal')
    
    df['legendaryproba'] = predictProba[:,1]
    df['prediction'] = predictions
    df.drop(['Legendary'], axis=1, inplace=True)
    
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

def callback_table_prediction(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children
    
def callbackpredict(n_clicks,name,type1,type2,generation,total,hp,attack,defense,spatk,spdef,speed) :
    if(name != '' and type1 != '' and type2 != '' 
    and generation != '' and total != '' 
    and hp != '' and attack != '' and defense != '' 
    and spatk != '' and spdef != '' and speed != '') :
        type1enc = encoderType1.transform([type1])[0]
        type2enc = encoderType2.transform([type2])[0]
        predictProba = loadModel.predict_proba([[type1enc,type2enc,int(total),
                                                int(hp), int(attack), 
                                                int(defense), int(spatk),
                                                int(spdef), int(speed), int(generation)]])
        prediction = 'Normal'
        predictSave = 0
        if(predictProba[0,1] > 0.15) :
            prediction = 'Legendary'
            predictSave = 1
        
        data = {
            'name': name,
            'type1': type1,
            'type2': type2,
            'total': int(total),
            'hp': int(hp),
            'attack': int(attack),
            'defense': int(defense),
            'spatk': int(spatk),
            'spdef': int(spdef),
            'speed': int(speed),
            'generation': int(generation),
            'legendary': predictSave,
            'legendaryproba': predictProba[0,1],
            'createdby': "Baron"
        }

        res = requests.post('http://api-pokemon-baron.herokuapp.com/saveprediction', data = data)
        print(res.content)

        return [
            html.H3('Probability your Pokemon is Legendary : {}%'.format(predictProba[0,1] * 100)),
            html.H3('so we predict {} is a {} Pokemon'.format(name,prediction))
        ]
    else :
        return html.H3('Please fill all inputs in the form above to Predict your Pokemon')