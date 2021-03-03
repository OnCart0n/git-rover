import subprocess
from lib.core.appdata import LDB


def _log(p: subprocess.Popen, key):
    try:
        while p.poll() is None:
            _ = p.stdout.readline()
            LDB[key] += _.decode()
    except KeyboardInterrupt:
        pass

def run_task(cmd:list, key:str):
    p = subprocess.Popen(' '.join(cmd), stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
    _log(p, key)
