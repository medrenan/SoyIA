from flask import request, jsonify,Blueprint,make_response

from controllers.general import hello
from controllers.aiMethods import getGrainsEstimate

general_bp = Blueprint("general",__name__)
aiMethods_bp = Blueprint("aiMethods",__name__)

@general_bp.route("/",methods=['GET'])
def sayHello():
    res = hello()
    return res

@aiMethods_bp.route("/getGrains/<id>",methods=['GET'])
def grainsEstimate(id):
    res = getGrainsEstimate(id)
    return res