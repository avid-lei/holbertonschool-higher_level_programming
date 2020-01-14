#!/usr/bin/python3
"""
Github Api to list recent commits
"""

if __name__ == '__main__':
    import sys
    import requests
    x = requests.get('https://api.github.com/repos/{}/{}/commits'.format
                    (sys.argv[2], sys.argv[1]))
    j = x.json()

    counter = 0

    for x in j:
        print("{}: {}".format
             (x.get('sha'), x.get('commit').get('author').get('name')))
        counter += 1
        if counter == 10:
            break
