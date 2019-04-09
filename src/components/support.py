legendDict = {
    'Legendary': { 'True': 'Legendary', 'False': 'Non-Legendary' },
    'Generation': { 1: '1st Generation', 
            2: '2nd Generation', 
            3: '3rd Generation', 
            4: '4th Generation',
            5: '5th Generation',
            6: '6th Generation'
    },
    'Type 1': { i:i for i in dfPokemon['Type 1'].unique()},
    'Type 2': { i:i for i in dfPokemon['Type 2'].unique()}
}