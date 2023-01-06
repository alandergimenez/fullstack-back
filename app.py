""" Mi App en Python """ 

from flask import Flask, request, redirect
import persistencia

app = Flask(__name__)

@app.route( "/pizza", methods=['POST'] )
def pizza():
    """ Guarda pedido """
    nombre    = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    persistencia.guardar_pedido(nombre, apellidos)
    print(nombre)    
    print(apellidos)
    return redirect("http://localhost/html/solicita_pedido.html", code=302)
app.run()
