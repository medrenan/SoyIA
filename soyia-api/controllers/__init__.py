from flask import request, jsonify,Blueprint,make_response

from controllers.general import hello
from controllers.aiMethods import getGrainsEstimate
from controllers.upload import fileUpload

general_bp = Blueprint("general",__name__)
aiMethods_bp = Blueprint("aiMethods",__name__)
fileUpload_bp = Blueprint("fileUpload",__name__)

@general_bp.route("/",methods=['GET'])
def sayHello():
    res = hello()
    return res

#Aqui ele recebe diretamente a string da imagem e retorna a estimativa
@aiMethods_bp.route("/getGrains",methods=['POST'])
def grainsEstimate():
    file = request.get_json()
    res = getGrainsEstimate(file)
    return res


@fileUpload_bp.route("/upload",methods=['POST'])
def uploadFile():
    file = request.get_json()['file']
    folderPath = request.get_json()['folderPath']

    if(file is None):
        res = make_response({"mensagem":'falta arquivo'},400)
        return res

    if(folderPath is None):
        res = make_response({"mensagem":'falta caminho'},400)
        return res
    
    res = fileUpload(file,folderPath)
    return res