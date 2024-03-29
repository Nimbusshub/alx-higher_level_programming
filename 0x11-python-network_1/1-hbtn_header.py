#!/usr/bin/python3
"""Python script that takes in a URL,
sends a request to the URL and displays the value of the X-Request-Id variable
found in the header of the response."""

if __name__ == '__main__':
    import urllib.request
    import sys

    url_req = urllib.request.Request(sys.argv[1])

    with urllib.request.urlopen(url_req) as response:
        url_res = response.info()
    print(url_res['X-Request-Id'])
