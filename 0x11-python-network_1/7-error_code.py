#!/usr/bin/python3
"""requests package error handling"""

if __name__ == "__main__":
    import sys
    import requests

    x = requests.get(sys.argv[1])
    if x.status_code >= 400:
        print('Error code: ' + str(x.status_code))
    else:
        print(x.text)
