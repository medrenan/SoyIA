from flask import make_response,jsonify

def getGrainsEstimate(cultiveId):
    return make_response({
        "sampleOne":{
            "plant1":20,
            "plant2":20,
        },
        "sampleTow":{
            "plant1":20,
            "plant2":20,
        },
        "sampleThree":{
            "plant1":20,
            "plant2":20,
        }
    },200)