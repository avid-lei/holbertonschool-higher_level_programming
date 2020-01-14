#!/usr/bin/python
"""github API"""

if __name__ == '__main__':
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    g = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))

    j = g.json()

    print(j['id'])
