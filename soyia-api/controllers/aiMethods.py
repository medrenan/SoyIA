from flask import make_response,jsonify
from imagem import IAprocess

#Substituir o 'test' pela imagem
teste = IAprocess('test')

def getGrainsEstimate(cultiveId):
    return make_response({
        "sampleOne":{
            "plant1": teste['graos']
        },
        "sampleTwo":{
            "plant1":20,
            "plant2":20,
        },
        "sampleThree":{
            "plant1":20,
            "plant2":20,
        }
    },200)