#!/usr/bin/python
# -*- encoding: utf-8 -*-


class BaseConfig:
    import configparser as _
    config = _.ConfigParser()
    config.read('config.ini')
    
    def __init__(self):
        for key in list(set(dir(self))-set(dir(BaseConfig))):
            t = getattr(self, key)
            if t is int:
                setattr(self, key, self.config.getint(self.__class__.__name__, key))
            elif t is str:
                setattr(self, key, self.config.get(self.__class__.__name__, key))
            elif t is bool:
                setattr(self, key, self.config.getboolean(self.__class__.__name__, key))
            # print(self.__class__.__name__, getattr(self, key))


class App(BaseConfig):
    name = str


class Config:
    app = App()


config = Config()
