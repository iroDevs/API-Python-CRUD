# API-Python-CRUD


## CRUD API em Python
- Esse projeto tem como objetivo criar uma API RESTful de exemplo utilizando Python e o framework Flask. Ele inclui as operações básicas de CRUD (Create, Read, Update e Delete) para um recurso de "itens".

 **Pré-requisitos**
- Python 3.x
- Flask
- Virtualenv (recomendado)

### Instalação
- Clone o repositório: git clone https://github.com/seu-usuario/crud-api-python.git
- Crie um ambiente virtual: python -m venv env
- Ative o ambiente virtual: source env/bin/activate (Linux/Mac) ou env\Scripts\activate (Windows)
- Instale as dependências: pip install -r requirements.txt
- Inicie o servidor: python main.py

A API possui as seguintes rotas:

GET /items: Retorna uma lista de todos os itens cadastrados
POST /items: Cria um novo item com as informações enviadas no corpo da requisição
GET /items/<id>: Retorna um item específico pelo ID
PUT /items/<id>: Atualiza um item específico pelo ID com as informações enviadas no corpo da requisição
DELETE /items/<id>: Exclui um item específico pelo ID

**Os itens são simplesmente objetos JSON com um ID e um nome, mas podem ser expandidos conforme necessário.**
