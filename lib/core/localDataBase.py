import os


_IS_WIN = os.name == "nt"
OSDIR = 'windows' if _IS_WIN else 'linux'

class LocalAppCheck:
    _hydra = False

    def __init__(self) -> None:
        self.refresh()
    
    def refresh(self):
        appname = 'hydra'
        setattr(self, '_'+appname, self.check_file(LocalDataBase.appdir+appname))

    @property
    def hydra(self):
        return self._hydra

    def check_file(self, dirpath):
        return True

class LocalDataBase(dict):
    appdir = './lib/app/'+OSDIR+'/'
    IS_WIN = _IS_WIN
