from flask import make_response,jsonify

def getGrainsEstimate(cultiveId):
    return make_response({"plant1":20},200)