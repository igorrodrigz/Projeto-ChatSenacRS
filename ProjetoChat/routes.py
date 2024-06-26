from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"]) 
def login():
    if (request.method='POST'):
        usuario = request.form['usuario']
        senha = request.form['senha']
    else:
        return render_template("telalogin.html")