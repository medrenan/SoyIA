import os
from dotenv import load_dotenv

load_dotenv()


databaseUser = os.getenv('databaseUser')
databasePassword = os.getenv('databasePassword')
databaseDBName = os.getenv('databaseDBName')
databaseHost = os.getenv('databaseHost')
port = os.getenv('port')
host = os.getenv('host')
privateKeyId = os.getenv('privateKeyId')
#privateKey= os.getenv('privateKey').replace('\\n', '\n')
projectId = os.getenv('projectId')
clientEmail = os.getenv('clientEmail')
clientId = os.getenv('clientId')
clientCertUrl = os.getenv('clientCertUrl')