from flask import Flask,jsonify,request 
from dotenv import load_dotenv
import os


load_dotenv()

api = Flask(__name__)

#Variaveis de ambiente
PORT = os.environ["PORT"]
HOST = os.environ["HOST"]
DEBUG = os.environ["DEBUG"]

print(PORT,HOST,DEBUG)

@api.route('/')
def obter_itens():
    return jsonify({'id': 1 ,'nome' : 'machado'})


api.run(debug=DEBUG,host=HOST,port=PORT)

