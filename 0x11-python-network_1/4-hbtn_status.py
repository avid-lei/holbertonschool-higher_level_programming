#!/usr/bin/python3
""" fetch with request package """

if __name__ == '__main__':
    import requests

    x = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print('\t- type: ' + str(type(x.text)))
    print('\t- content: ' + x.text)
