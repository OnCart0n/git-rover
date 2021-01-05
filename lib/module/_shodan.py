#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@Author  :   OnCart0n
'''


import sys
import json
import requests
import shodan

class ShodanPro:
    def __init__(self, key: str) -> None:
        self._api = shodan.Shodan(key)
    
    def search(self, query: str):
        return self._api.search(query)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Usage: %s <search query>' % sys.argv[0])
        sys.exit(1)
    try:
        api = ShodanPro('bW1pCgTLKMVV7f1bfxng9cfCKvWcwnTG')
        query = ''.join(sys.argv[1:])
        result = api.search(query)
        for service in result['matches']:
            print(service['ip_str'])
    except Exception as e:
        print('Error: %s' % e)
        sys.exit(1)
