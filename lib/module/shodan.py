#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@Author  :   OnCart0n
'''


import json
import requests
import shodan
import sys

class Shodan:
    SHODAN_API_KEY = 'insert your api key'
    if len(sys.argv) == 1:
        print('Usage: %s <search query>' % sys.argv[0])
        sys.exit(1)
    try:
        api = shodan.Shodan(SHODAN_API_KEY)
        query = ''.join(sys.argv[1:])
        result = api.search(query)
        for service in result['matches']:
            print(service['ip_str'])
    except Exception as e:
        print('Error: %s' % e)
        sys.exit(1)
    pass


if __name__ == "__main__":
    shodan = Shodan()
