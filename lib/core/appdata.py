#!/usr/bin/python
# -*- encoding: utf-8 -*-


from lib.core.config import config
from lib.module._fofa import Fofa
from lib.module._shodan import ShodanPro


fofa = Fofa(config.fofa.email, config.fofa.key)
shodan = ShodanPro(config.shodan.key)
