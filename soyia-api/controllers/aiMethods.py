from flask import make_response,jsonify

def getGrainsEstimate(cultiveId):
    return make_response({"grains":20},200)