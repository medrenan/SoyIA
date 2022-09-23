from flask import request, jsonify,Blueprint,make_response

from controllers.general import hello

general_bp = Blueprint("general",__name__)

@general_bp.route("/",methods=['GET'])
def sayHello():
    res = hello()
    return res