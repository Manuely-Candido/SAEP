from flask import Flask, redirect, render_template, request, session
from conexao import conectar
from datetime import timedelta

app = Flask("__name__")

app.secret_key = "uva"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

@app.route("/")
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        login = request.form.get("login")
        senha = request.form.get("senha")

        conexao, cursor = conectar()
        cursor.execute("""
                        SELECT login FROM usuario
                        WHERE login = %s
                        AND senha = %s
        """, [login, senha])
        usuario = cursor.fetchone()
        conexao.close()

        if usuario:
            session["usuario"] = usuario
            session.permanent = True
            return redirect("/principal")
        else:
            return "USUARIO OU SENHA INCORRETA"

@app.route("/principal")
def principal():
    return render_template("/principal")

@app.route("/logoff")
def logoff():
    session.clear()
    return redirect("/login")


app.run(debug=True)