#!/usr/bin/python3
""" request package post email """

if __name__ == '__main__':
    import sys
    import requests
    x = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(x.text)
