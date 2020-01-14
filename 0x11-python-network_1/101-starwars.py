#!/usr/bin/python3
"""star wars API"""

if __name__ == '__main__':
    import requests
    import sys

    x = requests.get('https://swapi.co/api/people/',
                     params={'search': sys.argv[1]})
    j = x.json()
    print('Number of results: {}'.format(j['count']))

    for i in j['results']:
        print(i['name'])
