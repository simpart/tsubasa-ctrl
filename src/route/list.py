from route import flask_app
from app.response import *
from app.list import *

@flask_app.route('/api/v1/list/<path:path>', methods=['GET'])
def list_items(path):
    # /api/v1/listの処理
    data = get_list('/' + path)
    return response(data)
