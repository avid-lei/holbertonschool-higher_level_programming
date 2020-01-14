#!/usr/bin/python3
"""Github Api to list recent commits"""

if __name__ == '__main__':
    import requests
    import sys
    x = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))

    counter = 0

    for j in x.json():
        print('{}: {}'.format(j.get('sha'), j.get('commit')
                              .get('author').get('name')))
        counter += 1
        if counter == 10:
            break;
