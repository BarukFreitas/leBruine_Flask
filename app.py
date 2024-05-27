from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/reservaConcluida")
def reservaConcluida():
    return render_template("reservaConcluida.html")

@app.route("/reservar")
def reservar():
    return render_template("reservar.html")



app.run(debug=True)