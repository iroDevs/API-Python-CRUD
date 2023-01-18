from flask import Flask,jsonify,request 
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from database.ItemBd import ItemBd


load_dotenv()

#Variaveis de ambiente
PORT = os.environ["PORT"]
HOST = os.environ["HOST"]
DEBUG = os.environ["DEBUG"]
URL_BASE = os.environ["URL_BASE"]
SQL_PORT = os.environ["SQL_PORT"]
DB_NAME = os.environ["DB_NAME"]

api = Flask(__name__)
# api.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{URL_BASE}:{SQL_PORT}/{DB_NAME}'
# db = SQLAlchemy(api)
ItemBd.run()

message_home = {
    "message": "boas vindas a minha api Teste",
    "entidade": "item",
    "rotas": ["GET -> /item","POST -> /item","PUT -> /item/<id>","DELETED /item/<id>","GET -> /item/<id>"]
}

#Rotas 
@api.route('/')
def obter_itens():
    return jsonify(message_home)


api.run(debug=DEBUG,host=HOST,port=PORT)
