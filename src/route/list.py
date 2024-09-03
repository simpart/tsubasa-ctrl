from route import app

@app.route('/api/v1/list', methods=['GET'])
def list_items():
    # /api/v1/listの処理
    return "List of items"
