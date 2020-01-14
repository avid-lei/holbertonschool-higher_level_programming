#!/usr/bin/python3
"""request package display value of variable"""

if __name__ == '__main__':
    import sys
    import requests

    x = requests.get(sys.argv[1])
    print(x.headers['X-Request-Id'])
