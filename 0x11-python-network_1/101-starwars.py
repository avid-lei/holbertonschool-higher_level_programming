#!/usr/bin/python3
"""star wars API"""

if __name__ == '__main__':
    import requests
    import sys

    x = requests.get('https://swapi.co/api/people/',
                     params={'search': sys.argv[1]})
    j = x.json()
    print('Number of results: {}'.format(j['count']))

    total = j['count']
    ctr = 0

    while (ctr != total):
        for i in j['results']:
            print(i['name'])
            ctr += 1
        if ctr == total:
            break
        x = requests.get(j['next'])
        j = x.json()
