from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

def converter_temperatura(valor, origem, destino):
    if origem == "celsius" and destino == "fahrenheit":
        return (valor * 9/5) + 32
    elif origem == "fahrenheit" and destino == "celsius":
        return (valor - 32) * 5/9

@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    resultado = None
    if request.method == "POST":
        temperatura = float(request.form["temperatura"])
        unidade_origem = request.form["unidade_origem"]
        unidade_destino = request.form["unidade_destino"]
        resultado = converter_temperatura(temperatura, unidade_origem, unidade_destino)
    return render_template("temperatura.html", resultado=resultado)


# Função para cálculo de operações matemáticas
@app.route("/matematica", methods=["GET", "POST"])
def matematica():
    resultado = None
    operacao = None  # Armazenar o tipo de operação

    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        operacao = request.form["operacao"]

        if operacao == "soma":
            resultado = num1 + num2
        elif operacao == "subtracao":
            resultado = num1 - num2
        elif operacao == "multiplicacao":
            resultado = num1 * num2
        elif operacao == "divisao":
            resultado = num1 / num2

    return render_template("matematica.html", resultado=resultado, operacao=operacao)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)