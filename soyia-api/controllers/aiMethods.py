import os
from flask import make_response,jsonify
from imagem import IAprocess, IATest

#Substituir o 'test' pela imagem e colocar False (metodo para a IA processar a imagem e retornar os dados)
teste = IAprocess('test',True)

#Metodo para medir a precisão do modelo
#IATest()

def getGrainsEstimate(cultiveId):
    return make_response({
        "sampleOne":{
            # "plant1": teste['graos']
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