#!/usr/bin/env python3

import json
import requests


URL = 'https://services.arcgis.com/5T5nSi527N4F7luB/arcgis/rest/services/Cases_by_country_pt_V3/FeatureServer/0/query'

def print_country_statistics(country):

    body = {
        "f": "json",
        "where": "ADM0_NAME LIKE '%{:s}%'".format(country),
        "returnGeometry": "false",
        "outFields": "ADM0_NAME,cum_conf,cum_death"
    }


    response = requests.post(URL, data=body)
    data = json.loads(response.text)


    try:
        result = data['features'][0]['attributes']
    except IndexError:
        print("Sorry, we couldn't lookup {:s}. Is there a spelling error?".format(country))
        sys.exit()
    print("Country: {:s}\nConfirmed cases: {:d}\nDeaths: {:d}".format(result['ADM0_NAME'],
                                                                      result['cum_conf'],
                                                                      result['cum_death']))

def print_total_statistics():

    out_statistics = [
       {
           'statisticType': 'sum',
           'onStatisticField': 'cum_conf',
           'outStatisticFieldName': 'tot_conf'
       },
       # I am unsure what these mean
       # {
       #     'statisticType': 'sum',
       #     'onStatisticField': 'cum_clin',
       #     'outStatisticFieldName': 'tot_clin'
       # }
       # {
       #     'statisticType': 'sum',
       #     'onStatisticField': 'cum_susp',
       #     'outStatisticFieldName': 'tot_susp'
       # }
       {
           'statisticType': 'sum',
           'onStatisticField': 'cum_death',
           'outStatisticFieldName': 'tot_death'
       },
       {
           'statisticType': 'count',
           'onStatisticField': 'cum_conf',
           'outStatisticFieldName': 'countries_affected'
       }
   ]

    body = {
        'f': 'json',
        'where': '1=1',
        'returnGeometry': 'false',
        'outStatistics': json.dumps(out_statistics)
    }

    response = requests.post(URL, data=body)
    data = json.loads(response.text)


    try:
        result = data['features'][0]['attributes']
    except IndexError:
        print("Sorry, we couldn't lookup {:s}. Is there a spelling error?".format(country))
        sys.exit()
    print("Total statistics:\nConfirmed cases: {:d}\nDeaths: {:d}\nCountries: {:d}".format(
        result['tot_conf'],
        result['tot_death'],
        result['countries_affected']
    ))
