#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
if __name__ == '__main__':
    import urllib.request

    url_req = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url_req) as response:
        res_req = response.read()
    print('Body response:')
    print('\t-', 'type:', type(res_req))
    print('\t-', 'content:', res_req)
    output = res_req.decode('utf_8')
    print('\t-', 'utf8 content:', output)
