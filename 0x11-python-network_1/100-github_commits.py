#!/usr/bin/python3
"""Github Api to list recent commits"""

if __name__ == '__main__':
    import sys
    import requests
    x = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))

    js = x.json()[:10]
    for j in js:
        print('{}: {}'.format(j.get('sha'), j.get('commit')
                              .get('author').get('name')))
