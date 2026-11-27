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

@app.route("/responsavel", methods=["GET", "POST"])
def responsavel():
    if request.method == "GET":
        busca = request.args.get("busca")
        conexao, cursor = conectar()
        if busca :
            cursor.execute("""
                            SELECT idresponsavel, nome, cpf FROM responsavel
                            WHERE nome like %s;
                        """, [f"%{busca}%"])
        else:
            cursor.execute("""
                                SELECT idresponsavel, nome, cpf FROM responsavel;
            """)
        responsaveis = cursor.fetchall()
        conexao.close()
        return render_template("responsavel.html", responsaveis = responsaveis)

    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")

        conexao, cursor = conectar()
        cursor.execute("""
                        INSERT INTO responsavel (cpf, nome)
                        VALUE (%s, %s);
        """, [cpf, nome])

        conexao.commit()
        conexao.close()
        return redirect ("/responsavel")


@app.route("/aluno", methods=["GET", "POST"])
def aluno():
    if request.method == "GET":
        conexao, cursor = conectar()
        cursor.execute("""
                            SELECT idresponsavel, nome, cpf FROM responsavel;
                        """)

        responsaveis = cursor.fetchall()
        conexao.close()
        return render_template("aluno.html", responsaveis = responsaveis)

    if request.method == "POST":
        nome = request.form.get("nome")
        idresponsavel = int(request.form.get("idresponsavel"))

        conexao, cursor = conectar()
        cursor.execute("""
                        INSERT INTO aluno (responsavel_idresponsavel, nome)
                        VALUE (%s, %s);
        """, [idresponsavel, nome])

        conexao.commit()
        conexao.close()
        return redirect ("/aluno")
    

@app.route("/excluir_responsavel/<idresponsavel>")
def excluir_responsavel(idresponsavel):
    conexao, cursor = conectar()
    cursor.execute("""
                    DELETE FROM responsavel 
                    WHERE idresponsavel = %s;
    """, [idresponsavel])
    
    conexao.commit()
    conexao.close()

@app.route("/alterar_responsavel", methods=["POST"])
def alterar_responsavel():
    idresponsavel = request.form.get("idresponsavel")
    cpf = request.form.get("cpf")
    nome = request.form.get("nome")

    conexao, cursor = conectar()
    cursor.execute("""
                    UPDATE responsavel 
                    SET cpf = %s,
                        nome = %s
                    WHERE idresponsavel = %s;
            """, [cpf, nome, idresponsavel])
    
    conexao.commit()
    conexao.close()
    return redirect("/responsavel")

app.run(debug=True)