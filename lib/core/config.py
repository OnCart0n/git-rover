#!/usr/bin/python
# -*- encoding: utf-8 -*-


config_file = 'config.ini'
from configparser import ParsingError

class BaseConfig:
    # 邪教写法
    import configparser as _
    config = _.ConfigParser()
    try:
        config.read(config_file)
    except ParsingError as e:
        print("请检查配置文件: ", repr(e).split('\n')[1].replace("\t", '').replace(' \\n', ''))
        exit()

    def __init__(self):
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


class Config:
    app = App()


config = Config()
