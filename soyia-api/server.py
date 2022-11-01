from flask import Flask,request
from flask_cors import CORS
from models.envVariables import port,host
from controllers import general_bp,aiMethods_bp,fileUpload_bp
from db.firebase import firebase_setup

app = Flask(__name__)
CORS(app)
app.register_blueprint(general_bp)
app.register_blueprint(aiMethods_bp)
app.register_blueprint(fileUpload_bp)

firebase_setup()

@app.after_request
def after_request(response):
    try:
        white_origin= ['http://www.dom.com:8000','http://localhost']
        if request.headers['Origin'] in white_origin:
            response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
            response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        return response
    except:
        return response

if __name__ == '__main__':
    app.run(port=port,host=host)