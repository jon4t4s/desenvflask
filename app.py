from flask import Flask, render_template, request, redirect, url_for

app_Jonatas = Flask(__name__)

@app_Jonatas.route('/')
def login():
    return render_template('login.html')

@app_Jonatas.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == "__main__":
    app_Jonatas.run(debug=True)
