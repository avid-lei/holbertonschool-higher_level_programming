#!/usr/bin/python3
"""star wars API"""

if __name__ == '__main__':
    import requests
    import sys

    x = requests.get('https://swapi.co/api/people/',
                     params={'search': sys.argv[1]})
    j = x.json()
    print('Number of results: {}'.format(j.get('count')))

    total = j.get('count')
    ctr = 0

    while (ctr != total):
        for i in j.get('results'):
            print(i.get('name'))
            ctr += 1
            for f in i.get('films'):
                fg = requests.get(f)
                print('\t' + fg.json().get('title'))

        if ctr == total:
            break
        x = requests.get(j.get('next'))
        j = x.json()