#!/usr/bin/env python3

import json
import requests

def print_statistics():
    url = 'https://services6.arcgis.com/L1SotImj1AAZY1eK/arcgis/rest/services/COVID19__Regioni/FeatureServer/0/query'

    out_statistics = [
        {
            "statisticType": "sum",
            "onStatisticField": "ricoverati_con_sintomi",
            "outStatisticFieldName": "hospitalized_with_symptoms"
        },
        {
            "statisticType": "sum",
            "onStatisticField": "terapia_intensiva",
            "outStatisticFieldName": "intensive_care"
        },
        {
            "statisticType": "sum",
            "onStatisticField": "totale_ospedalizzati",
            "outStatisticFieldName": "total_hospitalized"
        },
        {
            "statisticType": "sum",
            "onStatisticField": "isolamento_domiciliare",
            "outStatisticFieldName": "home_isolation"
        },
        {
            "statisticType": "sum",
            "onStatisticField": "totale_attualmente_positivi",
            "outStatisticFieldName": "total_currently_positive"
        },
        {
            "statisticType": "sum",
            "onStatisticField": "nuovi_attualmente_positivi",
            "outStatisticFieldName": "new_currently_positive"
        },
        {
            "statisticType": "sum",
            "onStatisticField": "dimessi_guariti",
            "outStatisticFieldName": "discharged_healed"
        },
        {
            "statisticType": "sum",
            "onStatisticField": "deceduti",
            "outStatisticFieldName": "deceased"
        },
        {
            "statisticType": "sum",
            "onStatisticField": "totale_casi",
            "outStatisticFieldName": "total_cases"
        },
        {
            # Is this a number of tests performed??
            "statisticType": "sum",
            "onStatisticField": "tamponi",
            "outStatisticFieldName": "tamponi"
        }
    ]

    body = {
        'f': 'json',
        'where': 'totale_casi > 0',
        'returnGeometry': 'false',
        'outStatistics': json.dumps(out_statistics)
    }

    response = requests.post(url, data=body)
    data = json.loads(response.text)

    try:
        result = data['features'][0]['attributes']
    except IndexError:
        print('Something went terribly wrong')
        sys.exit()

    print("""Country: Italy
    Hospitalized with symptoms: {:d}
    Intensive care: {:d}
    Total hospitalized: {:d}
    Home isolation: {:d}
    Total currently positive: {:d}
    New currently positive: {:d}
    Discharged healed: {:d}
    Deceased: {:d}
    Total cases: {:d}
    Tamponi: {:d}""".format(result['hospitalized_with_symptoms'],
               result['intensive_care'],
               result['total_hospitalized'],
               result['home_isolation'],
               result['total_currently_positive'],
               result['new_currently_positive'],
               result['discharged_healed'],
               result['deceased'],
               result['total_cases'],
               result['tamponi']
    ))
