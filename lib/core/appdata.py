#!/usr/bin/python
# -*- encoding: utf-8 -*-


from lib.core.config import Config
from lib.module._fofa import Fofa
from lib.module._shodan import ShodanPro
from lib.core.localDataBase import LocalAppCheck, LocalDataBase


config = Config()

fofa = Fofa(config.fofa.email, config.fofa.key)
shodan = ShodanPro(config.shodan.key)

LAC = LocalAppCheck()
LDB = LocalDataBase()
