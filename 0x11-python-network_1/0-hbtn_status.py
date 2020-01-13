#!/usr/bin/python3
"""python script fetches website"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as x:
    d = x.read()
    print('Body response:')
    print(f'\t- type: {type(d)}')
    print(f'\t- content: {d}')
    print(f'\t- utf8 content: {d.decode("utf-8")}')
