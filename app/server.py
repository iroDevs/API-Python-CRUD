from flask import Flask,jsonify,request 
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

#Variaveis de ambiente
PORT = os.environ["PORT"]
HOST = os.environ["HOST"]
DEBUG = os.environ["DEBUG"]
URL_BASE = os.environ["URL_BASE"]
SQL_PORT = os.environ["SQL_PORT"]
DB_NAME = os.environ["DB_NAME"]

api = Flask(__name__)
api.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{URL_BASE}:{SQL_PORT}/{DB_NAME}'
db = SQLAlchemy(api)


#Rotas 
@api.route('/')
def obter_itens():
    return jsonify({'id': 1 ,'nome' : 'machado'})


api.run(debug=DEBUG,host=HOST,port=PORT)
