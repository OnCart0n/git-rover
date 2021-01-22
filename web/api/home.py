from flask import Blueprint


api = Blueprint('home', __name__)


@api.route('/')
def home():
    # 目前只是展示用法，具体状态码及返回内容再定
    return {'code': 20000, 'message': 'Is Working!', 'data': None}
