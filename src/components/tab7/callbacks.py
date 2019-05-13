from src.components.dataPokemon import dfHistory,dfHistoryTable
from src.components.tab7.view import generate_table

def callbacksortingtablehistory(pagination_settings, sorting_settings) :
    # print(sorting_settings)
    if len(sorting_settings):
        dff = dfHistoryTable.sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = dfHistoryTable

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')

def callbackfiltertablehistory(createdby,maxrows) :   
    global dfHistoryTable
    dfHistoryTable = dfHistory[dfHistory['createdby'].str.contains(createdby, case=False)]
    return generate_table(dfHistoryTable, pagesize=maxrows)