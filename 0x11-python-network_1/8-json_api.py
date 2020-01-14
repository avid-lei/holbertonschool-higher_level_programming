#!/usr/bin/python3
"""search API with requests package"""

if __name__ == '__main__':
    import sys
    import requests
    if len(sys.argv) < 2:
        param = ""
    else:
        param = sys.argv[1]

    x = requests.post('http://0.0.0.0:5000/search_user', data={'q': param})
    try:
        j = x.json()
        if j == {}:
            print('No result')
        else:
            print('[{}] {}'. format(j['id'], j['name']))
    except ValueError:
        print('Not a valid JSON')
