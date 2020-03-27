#!/usr/bin/env python3

import json
import requests

# This is the official Lithuanian database (or however else you call ArcGIS)
URL = 'https://services.arcgis.com/XdDVrnFqA9CT3JgB/arcgis/rest/services/covid_statistics/FeatureServer/0/query'

def print_statistics():

    body = {
        'f': 'json',
        'where': '1=1',
        'outFields': '*',
        'orderByFields': 'Data desc',
        'resultRecordCount': 1,
    }
    response = requests.post(URL, data=body)
    data = json.loads(response.text)

    try:
        result = data['features'][0]['attributes']
    except IndexError:
        print('Something went terribly wrong')
        sys.exit()

    print("""Country: Lithuania
    Confirmed cases: {:d}
    Active cases: {:d}
    Recovered: {:d}
    Deaths: {:d}
    Cases per day: {:d}""".format(result['Atvejų_skaičius'],
                                  result['Aktyvūs_atvejai'],
                                  result['Pasveikimai'],
                                  result['Mirtys'],
                                  result['Atvejai_per_dieną'],
    ))
