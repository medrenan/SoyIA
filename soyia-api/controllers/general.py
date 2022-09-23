from flask import make_response,jsonify

def hello():
    return make_response({"mensagem":"Hello World"},200)