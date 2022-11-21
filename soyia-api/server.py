import sys
sys.path.insert(0, "../IA")
from flask import Flask,request
from flask_cors import CORS
from models.envVariables import port,host
from controllers import general_bp,aiMethods_bp,fileUpload_bp
#from db.firebase import firebase_setup

app = Flask(__name__)
CORS(app)
app.register_blueprint(general_bp)
app.register_blueprint(aiMethods_bp)
app.register_blueprint(fileUpload_bp)

#firebase_setup()



if __name__ == '__main__':
    app.run(port=port,host=host)