from flask import jsonify, make_response

def response(data, status_code=200):
    conts = {
        'code':  status_code,
        'error': None,
        'data':  data
    }
    resp = make_response(jsonify(conts), status_code)
    resp.headers['Content-Type'] = 'application/json'
    return resp
    

