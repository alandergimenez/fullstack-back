""" Mi App en Python """

from flask import Flask, request, redirect, Response
import persistencia

app = Flask(__name__)

@app.route("/pizza", methods=['POST'])
def pizza():
    """ Guarda pedido """
    nombre    = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    persistencia.guardar_pedido(nombre, apellidos)
    print(nombre)
    print(apellidos)
    return redirect("http://localhost/html/solicita_pedido.html", code=302)


@app.route("/checksize", methods=['POST'])
def checksize():
    """  Comprueba disponibilidad de un tamaño de pizza.  """

    tamano  = request.form.get("tamano")

    print(tamano)

    if tamano == "S":
        mensaje = "No disponsible"
        return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})

    elif tamano == "N":
        mensaje = ""
        return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})

    else:
        mensaje = "Disponsible"
        return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})

app.run()
