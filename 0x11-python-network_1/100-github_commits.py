#!/usr/bin/python3
"""Github Api to list recent commits"""

if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    for commit in r.json()[0:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))
