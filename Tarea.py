from flask import Flask, request, jsonify #importamos las librerias necesarias

# Crear la app
app = Flask(__name__)


# -----------------------------
# 1) GET /saludo
# -----------------------------
@app.route("/saludo", methods=["GET"]) #decorador para definir la ruta y el método HTTP
def saludo(): #función que se ejecuta cuando se accede a la ruta /saludo con el método GET
    return jsonify({ #devolvemos una respuesta en formato JSON
        "mensaje": "API de Calculadora funcionando" #clave "mensaje" con el valor "API de Calculadora funcionando"
    })


# -----------------------------
# 2) GET /cuadrado/<numero>
# -----------------------------
@app.route("/cuadrado/<int:numero>", methods=["GET"]) #decorador para definir la ruta y el método HTTP, con un parámetro de tipo entero llamado "numero"
def cuadrado(numero): #función que se ejecuta cuando se accede a la ruta /cuadrado con el método GET

    resultado = numero * numero #calculamos el cuadrado del número recibido como parámetro

    return jsonify({ #devolvemos una respuesta en formato JSON
        "numero": numero, #clave "numero" con el valor del número recibido como parámetro
        "resultado": resultado #clave "resultado" con el valor del cuadrado del número
    })


# -----------------------------
# 3) POST /operacion
# -----------------------------
@app.route("/operacion", methods=["POST"]) #decorador para definir la ruta y el método HTTP, en este caso es POST porque vamos a recibir datos en el cuerpo de la solicitud
def operacion(): # función que se ejecuta cuando se accede a la ruta /operacion con el método POST

    datos = request.json #obtenemos los datos enviados en el cuerpo de la solicitud, que se espera que sean un JSON con las claves "a", "b" y "operacion"

    a = datos.get("a") #obtenemos el valor de "a" del JSON recibido
    b = datos.get("b") #obtenemos el valor de "b" del JSON recibido
    op = datos.get("operacion") #obtenemos el valor de "operacion" del JSON recibido, que se espera que sea una cadena con el nombre de la operación a realizar (suma, resta, multiplicacion o division)

    if op == "suma": #si la operación es "suma", realizamos la suma de a y b
        resultado = a + b #almacenamos el resultado de la suma en la variable "resultado"

    elif op == "resta": # si la operación es "resta", realizamos la resta de a y b
        resultado = a - b #almacenamos el resultado de la resta en la variable "resultado"

    elif op == "multiplicacion": # si la operación es "multiplicacion", realizamos la multiplicación de a y b
        resultado = a * b #almacenamos el resultado de la multiplicación en la variable "resultado"

    elif op == "division": # si la operación es "division", realizamos la división de a y b, pero primero verificamos que b no sea 0 para evitar un error de división por cero

        if b == 0: #si b es 0, devolvemos un error en formato JSON indicando que no se puede dividir entre 0
            return jsonify({ #devolvemos una respuesta en formato JSON
                "error": "No se puede dividir entre 0" #clave "error" con el valor "No se puede dividir entre 0"
            })

        resultado = a / b #si b no es 0, realizamos la división de a y b y almacenamos el resultado en la variable "resultado"

    else: #si la operación no es ninguna de las anteriores, devolvemos un error en formato JSON indicando que la operación es inválida
        return jsonify({ #devolvemos una respuesta en formato JSON
            "error": "Operacion invalida" #clave "error" con el valor "Operacion invalida"
        })

    return jsonify({ #devolvemos una respuesta en formato JSON con los valores de a, b, la operación realizada y el resultado
        "a": a, #clave "a" con el valor de a recibido en el JSON
        "b": b, #clave "b" con el valor de b recibido en el JSON
        "operacion": op, #clave "operacion" con el valor de la operación realizada (suma, resta, multiplicacion o division)
        "resultado": resultado #clave "resultado" con el valor del resultado de la operación realizada
    })


# -----------------------------
# Ejecutar la app
# -----------------------------
if __name__ == "__main__": #si este archivo se ejecuta directamente (en lugar de ser importado como un módulo), se ejecuta el bloque de código dentro de esta condición
    app.run(debug=True) # iniciamos la aplicación Flask en modo de depuración (debug=True) para facilitar el desarrollo y la detección de errores. La aplicación estará disponible en http://localhost:5000/ por defecto.