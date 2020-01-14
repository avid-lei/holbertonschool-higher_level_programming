#!/usr/bin/python3
""" fetch with request package """

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as x:
        s = x.read().decode('utf-8')
        print("Body response:")
        print('\t- type: ' + str(type(s)))
        print('\t- content: ' + s)
