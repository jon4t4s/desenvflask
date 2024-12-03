from flask import Flask, render_template, request, redirect, url_for, flash
import re

app_Jonatas = Flask(__name__)
app_Jonatas.secret_key = 'chave_secreta'

@app_Jonatas.route('/', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app_Jonatas.route('/cadastro', methods=['GET','POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        senha1 = request.form['senha1']
        senha2 = request.form['senha2']

        # Verifica se as senhas coincidem
        if senha1 != senha2:
            flash("As senhas não coincidem! Tente novamente.", "error")
            return redirect(url_for('cadastro'))
        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app_Jonatas.route('/home_page')
def home_page():
    return render_template('home_page.html')

@app_Jonatas.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == "__main__":
    app_Jonatas.run(debug=True)
