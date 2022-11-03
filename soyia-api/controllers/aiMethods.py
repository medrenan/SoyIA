from flask import make_response,jsonify
# from imagem import IAprocess


def getGrainsEstimate(cultiveId):
    #Substituir o 'test' pela imagem
    teste = IAprocess('test')
    res = teste['graos']

    if(res is not None):
        return make_response(res)
    
    
    return make_response({
        "sample":{
            "grains":20,
            "pods":20,
        }
    },200)