#!/usr/bin/python3
"""Error handling with urllib"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error
    try:
        with urllib.request.urlopen(sys.argv[1]) as x:
            print(x.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: " + str(e.code))
