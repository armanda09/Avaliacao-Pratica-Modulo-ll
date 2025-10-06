from flask import Flask, request, render_template, jsonify#precisa
app = Flask(__name__)#precisa

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/soma", methods=['GET'])
def get_soma():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    somar = valor1 + valor2
    return jsonify({"Resultado": somar})

@app.route("/subtrair", methods=['GET'])
def get_subtrair():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    subtrair = valor1 - valor2
    return jsonify({"Resultado": subtrair})

@app.route("/multiplicar", methods=['GET'])
def get_multiplica():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    multiplicar = valor1 * valor2
    return jsonify({"Resultado": multiplicar})

@app.route("/dividir", methods=['GET'])
def get_dividir():
    valor1 = float(request.args.get("valor1"))
    valor2 = float(request.args.get("valor2"))
    if valor2 == 0:
        return {"erro": "Divisão por zero não é perimitida!"}
    dividir = valor1 / valor2
    return jsonify({"Resultado": dividir})


if __name__ == '__main__':
    app.run(debug=True)#app.run precisa