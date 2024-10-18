from app import app
from flask import render_template
from flask import request
import requests
import json
link = "https://flasktintgrazy-default-rtdb.firebaseio.com/"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Inicial")
@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contatos")
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastrar")

@app.route('/exxcluir')
def exxcluir():
    return render_template('exxcluir.html', titulo="Exxcluir")

@app.route('/atualizar')
def atualizar():
    return render_template('atualizar.html', titulo="atualizar")




@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf    = request.form.get("cpf")
        nome   = request.form.get("nome")
        telefone    = request.form.get("telefone")
        endereco    = request.form.get("endereco")
        pagamento   = request.form.get("pagamento")
        dados   = {'cpf': cpf, "nome": nome, "telefone": telefone, "endereco": endereco, "pagamento":pagamento}
        requisitos = requests.post(f'{link}/cadastro/.json', data = json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n +{e}'

@app.route('/Listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Ocorreu um erro\n +{e}'

@app.route('/ListarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '666666666':
               idCadastro = codigo
               return idCadastro
    except Exception as e:
        return f'Ocorreu um erro\n +{e}'




@app.route('/atualize',methods=['POST'])
def atualize():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        dados = {'cpf': cpf, 'nome': nome}
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == cpf:
                requisicao = requests.patch(f'{link}/cadastro/{codigo}/.json', data=json.dumps(dados))
                return 'Atualizado com sucesso!'
    except Exception as e:
        return f'Algo deu errado\n + {e}'




@app.route('/excluir', methods=['POST'])
def excluir():
    try:

        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = ""
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")

        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']


        requisicao = requests.delete(f'{link}/cadastro/{idCadastro}/.json')
        return "Excluido com sucesso!"
    except Exception as e:
        return f'Algo deu errado\n +{e}'


