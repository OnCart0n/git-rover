import threading
from lib.core.appdata import LDB


class BaseModule(threading.Thread):
    dir = 'linux'
    appname = 'change'

    @property
    def app_path(self):
        return LDB.appdir+self.dir+'/'+self.appname