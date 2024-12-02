from flask import Flask, render_template, request, redirect, url_for

app_Jonatas = Flask(__name__)

@app_Jonatas.route('/', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app_Jonatas.route('/cadastro', methods=['GET','POST'])
def cadastro():
    return render_template('cadastro.html')

@app_Jonatas.route('/home_page')
def home_page():
    return render_template('home_page.html')

@app_Jonatas.route('/sobre')
def sobre():
    return render_template('sobre.html')

if __name__ == "__main__":
    app_Jonatas.run(debug=True)
