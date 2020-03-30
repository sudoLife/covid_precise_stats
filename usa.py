#!/usr/bin/env python3

import json
import requests
from bs4 import BeautifulSoup

URL = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
}

def print_statistics():
    # okay so I couldn't find a proper centralized API yet. Let's crawl.
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
#    print(soup.prettify())

    cases = soup.find('div', attrs={'class': 'card-body bg-white'}).ul.find_all('li')
    arr = cases[0].string[len('Total cases: '):].split(',')

    total_cases = 0
    total_deaths = 0

    for elem in arr:
        total_cases *= 1000
        total_cases += int(elem)

    arr = cases[1].string[len('Total deaths: '):].split(',')

    for elem in arr:
        total_deaths*= 1000
        total_deaths += int(elem)


    print("""Country: United States
    Confirmed cases: {:d}
    Confirmed deaths: {:d}""".format(total_cases,
                                 total_deaths
    ))
