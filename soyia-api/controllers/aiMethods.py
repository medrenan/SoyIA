import os
from flask import make_response,jsonify
from imagem import IAprocess, IATest

#Metodo para medir a precisão do modelo (usar apenas para gerar as métricas de precisão dele)
#IATest()

def getGrainsEstimate(imageStr):
    # return make_response({"pods":20,"grains":20},200)
    res = IAprocess(imageStr,False,0)
    return make_response({"pods": res["vagens"], "grains": res["graos"]},200)

