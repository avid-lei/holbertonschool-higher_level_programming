#!/usr/bin/python3
"""Github Api to list recent commits"""

if __name__ == '__main__':
    import requests
    import sys
    x = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))

    for j in x.json()[:10]:
        print('{}: {}'.format(j.get('sha'), j.get('commit')
                              .get('author').get('name')))
