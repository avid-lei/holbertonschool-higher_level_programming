#!/usr/bin/python3
"""python script fetches website"""

if __name__ == '__main__':
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as x:
        d = x.read()
        print('Body response:')
        print('\t- type: ' + str(type(d)))
        print('\t- content: ' + str(d))
        print('\t- utf8 content: ' + d.decode("utf-8"))
