class RespData:
    @staticmethod
    def error(message='error', data=None):
        return {'code': 40000, 'message': message, 'data': data}
    
    def success(message='success', data=None):
        return {'code': 20000, 'message': message, 'data': data}
