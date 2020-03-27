#!/usr/bin/env python3
import json
import sys
import requests
import getopt

#importing countries
import italy
import lithuania
import who



def print_country(country):
    # This is where all the countries should be added later
    if country == 'Lithuania':
        lithuania.print_statistics()
        return
    elif country == 'Italy':
        italy.print_statistics()
        return
    else:
        who.print_country_statistics(country)



def main():
    try:
        opts = getopt.gnu_getopt(sys.argv[1:], 'c:t', ['country=', 'total'])[0]
    except getopt.GetoptError as err:
        print(err.msg)
        sys.exit()

    for opt, val in opts:
        if opt in ['-c', '--country']:
            print_country(val)
        elif opt in ['-t', '--total']:
            who.print_total_statistics()

if __name__ == "__main__":
    main()
