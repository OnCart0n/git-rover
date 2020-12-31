#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@Author  :   OnCart0n
'''

import json
import base64
import requests


class Fofa:
    def __init__(self, email: str, key: str) -> None:
        self.email = email
        self.key = key
        self.base_api = 'https://fofa.so'
        self.search_api = '/api/v1/search/all'
        self.login_api = '/api/v1/info/my'
        self.get_userinfo()
    
    def get_userinfo(self) -> dict:
        api_full_url = '%s%s' % (self.base_api, self.login_api)
        param = {'email': self.email, 'key': self.key}
        r = self.__http_get(api_full_url, param)
        return json.loads(r)
    
    def search(self, query_str: str, page=1, fields='') -> dict:
        api_full_url = '%s%s' % (self.base_api, self.search_api)
        param = {'qbase64': base64.b64encode(query_str.encode()).decode(), 'email': self.email, 'key': self.key, 'page': page, 'fields': fields}
        res = self.__http_get(api_full_url, param)
        return json.loads(res)
    
    def __http_get(self, url: str, param: dict) -> str:
        try:
            res = requests.get(url, param).text
            if "errmsg" in res:
                raise RuntimeError(res)
        except Exception as e:
            raise e
        return res
