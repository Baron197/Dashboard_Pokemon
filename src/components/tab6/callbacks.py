import pickle
import requests
import dash_html_components as html
loadModel = pickle.load(open('rfc_pokemon.sav', 'rb'))
encoderType1 = pickle.load(open('le_type1.sav', 'rb'))
encoderType2 = pickle.load(open('le_type2.sav', 'rb'))

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