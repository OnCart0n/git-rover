from lib.core.appdata import LDB
from lib.utils._random import get_random_chr
from lib.core.cmd_pipe import run_task
from ._BaseModule import BaseModule


class Hydra(BaseModule):
    def init(self, host, port, service):
        self.dir = 'hydra'
        self.appname = 'hydra.exe' if LDB.IS_WIN else 'hydra'
        self.host = host
        self.port = str(port)
        self.service = service

        self.key = get_random_chr()
        LDB[self.key] = ''
        return self.key 
    
    def run(self) -> None:
        cmd = [self.app_path, '-l', 'admin', '-p', 'password', self.host, self.service]
        run_task(cmd, self.key)
