from flask import Flask

app_Jonatas = Flask (__name__)

@app_Jonatas.route('/')
@app_Jonatas.route('/rota1')

def rota1():
    return 'Olá, Jônatas Dias!'

def saudacoes (nome):
    return f'Olá,{nome}'

if __name__ == "__main__":

    app_Jonatas.run()
    
