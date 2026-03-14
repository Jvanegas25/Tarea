from flask import Flask, request, jsonify

# Crear la app
app = Flask(__name__)


# -----------------------------
# 1) GET /saludo
# -----------------------------
@app.route("/saludo", methods=["GET"])
def saludo():
    return jsonify({
        "mensaje": "API de Calculadora funcionando"
    })


# -----------------------------
# 2) GET /cuadrado/<numero>
# -----------------------------
@app.route("/cuadrado/<int:numero>", methods=["GET"])
def cuadrado(numero):

    resultado = numero * numero

    return jsonify({
        "numero": numero,
        "resultado": resultado
    })


# -----------------------------
# 3) POST /operacion
# -----------------------------
@app.route("/operacion", methods=["POST"])
def operacion():

    datos = request.json

    a = datos.get("a")
    b = datos.get("b")
    op = datos.get("operacion")

    if op == "suma":
        resultado = a + b

    elif op == "resta":
        resultado = a - b

    elif op == "multiplicacion":
        resultado = a * b

    elif op == "division":

        if b == 0:
            return jsonify({
                "error": "No se puede dividir entre 0"
            })

        resultado = a / b

    else:
        return jsonify({
            "error": "Operacion invalida"
        })

    return jsonify({
        "a": a,
        "b": b,
        "operacion": op,
        "resultado": resultado
    })


# -----------------------------
# Ejecutar la app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)