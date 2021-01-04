#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@Author  :   OnCart0n
'''


import json
import requests
import shodan


class Shodan:
    SHODAN_API_KEY = 'insert your key here'
    api = shodan.Shodan(SHODAN_API_KEY)
    pass


if __name__ == "__main__":
    shodan = Shodan()
