from flask import Flask, render_template, request, redirect, session
from hashlib import sha256
from conexao import Conexao
app = Flask(__name__)


@app.route("/")
def pagina_inicial():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)