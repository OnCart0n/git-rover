#!/usr/bin/python
# -*- encoding: utf-8 -*-

import configparser


class BaseConfig:
    def __init__(self, config_file='config.ini'):
        try:
            self.config = configparser.ConfigParser()
            self.config.read(config_file)
        except configparser.ParsingError as e:
            raise Exception("请检查配置文件: " + repr(e).split('\n')[1].replace("\t", '').replace('\\n', ''))

        for key in list(set(dir(self))-set(dir(BaseConfig))):
            t = getattr(self, key)
            if t is int:
                setattr(self, key, self.config.getint(self.__class__.__name__, key))
            elif t is str:
                setattr(self, key, self.config.get(self.__class__.__name__, key))
            elif t is bool:
                setattr(self, key, self.config.getboolean(self.__class__.__name__, key))


class App(BaseConfig):
    name = str
    debug = bool


class Shodan(BaseConfig):
    key = str


class Fofa(BaseConfig):
    email = str
    key = str


class Config:
    app = App()
    shodan = Shodan()
    fofa = Fofa()
