from flask import Blueprint, request
from lib.core.appdata import LDB
from lib.module._hydra import Hydra
from web.core.respdata import RespData


api = Blueprint('scan', __name__)


@api.route('/hydra', methods=['GET', 'POST'])
def scan_hydra():
    data = request.json
    hydra = Hydra()
    key = hydra.init(data['host'], data['port'], data['service'])
    print(1)
    hydra.start()
    print(2)
    return RespData.success(data={'key': key})

@api.route('/hydra/<string:key>')
def data_hydra(key: str):
    return LDB[key]
