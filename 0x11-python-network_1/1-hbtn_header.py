#!/usr/bin/python3
"""take in URL, send request and display value of vairable found in header"""


if __name__ == '__main__':
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as x:
        print(x.headers['X-Request-Id'])
