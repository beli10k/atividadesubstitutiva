from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    titulo = "Google Fake"
    return render_template("index.html", titulo=titulo)

@app.route("/imagens")
def imagens():
    titulo = "Google Imagens Fake"
    return render_template("images.html", titulo=titulo)

@app.route("/advanced")
def advanced():
    titulo = "Pesquisa Avançada"
    return render_template("advanced.html", titulo=titulo)

# Exemplo de redirect (obrigatório no trabalho)
@app.route("/gooogle")
def errado():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
