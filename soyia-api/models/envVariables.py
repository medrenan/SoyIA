import os
from dotenv import load_dotenv

load_dotenv()


databaseUser = os.getenv('databaseUser')
databasePassword = os.getenv('databasePassword')
databaseDBName = os.getenv('databaseDBName')
databaseHost = os.getenv('databaseHost')
port = os.getenv('port')
host = os.getenv('host')
